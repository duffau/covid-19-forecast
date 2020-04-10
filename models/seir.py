from typing import Iterable
from .model import Model
from .params import SEIRParams
import models.utils as ut

from scipy.integrate import solve_ivp
from scipy.optimize import minimize
import numpy as np


class SEIR(Model):
    FIT_PARAMS_LOWER = np.array([0.0, -1e-15, -1e-15, -1e-15])
    FIT_PARAMS_UPPER = np.array([5.0, 1.0, 1.0, 1.0])

    def __init__(self, params: SEIRParams, seed=42):
        if not params:
            params = SEIRParams.from_random(seed=seed)
        super().__init__(params)

    def fit(self, y_obs, t_eval, options=None):
        _options = {'maxiter': 2500, 'maxfev': 5000}
        if options:
            _options.update(options)

        res = minimize(
            fun=self._minimize_wrapper,
            x0=self.free_params,
            args=(y_obs, t_eval),
            method='Nelder-Mead',
            options=_options
        )
        print(res)

    @property
    def free_params(self):
        param_lower = self.FIT_PARAMS_LOWER
        param_upper = self.FIT_PARAMS_UPPER
        selected_params = np.array([self.params.beta, self.params.E0,  self.params.I0, self.params.R0])
        return self.repam(selected_params, param_lower, param_upper)

    def _minimize_wrapper(self, fit_params, y_obs, t_eval):
        # print(f'fit_params: {fit_params}')
        param_lower = self.FIT_PARAMS_LOWER
        param_upper = self.FIT_PARAMS_UPPER
        beta, E0, I0, R0 = self.inv_repam(fit_params, param_lower, param_upper)
        # print(f'beta, I0, E0, R0: {beta, I0, E0, R0}')
        gamma = None
        alpha = None
        S0 = None
        self._update_params(beta, gamma, alpha, S0, E0, I0, R0)
        return self._sum_sq(y_obs, t_eval)

    def inv_repam(self, fit_params, lower, upper):
        return ut.sigmoid(fit_params, lower, upper)

    def repam(self, fit_params, lower, upper):
        return ut.inv_sigmoid(fit_params, lower, upper)

    def _sum_sq(self, y_obs, t_eval):
        S_hat_t, E_hat_t, I_hat_t, R_hat_t = self.simulate(t_eval=t_eval)
        S_t, E_t, I_t, R_t = y_obs
        val = 0
        val += ((S_hat_t - S_t) ** 2).mean()
        val += ((I_hat_t - I_t) ** 2).mean()
        val += ((R_hat_t - R_t) ** 2).mean()
        # print(f'sum_sq: {val}')
        return val

    def _update_params(self, beta, gamma, alpha, S0, E0, I0, R0):
        if beta is not None:
            self.params.beta = beta
        if gamma is not None:
            self.params.gamma = gamma
        if alpha is not None:
            self.params.alpha = alpha
        if S0 is not None:
            self.params.S0 = S0
        if E0 is not None:
            self.params.E0 = E0
        if I0 is not None:
            self.params.I0 = I0
        if R0 is not None:
            self.params.R0 = R0

    def _deriv(self, t, y, beta, gamma, alpha):
        S, E, I, R = y
        dSdt = -beta * S * I
        dEdt = beta * S * I - alpha * E
        dIdt = alpha * E - gamma * I
        dRdt = gamma * I
        return dSdt, dEdt, dIdt, dRdt

    def simulate(self, t_eval: Iterable[float], N=1.0):
        y0 = (self.params.S0, self.params.E0, self.params.I0, self.params.R0)
        t_span = (min(t_eval), max(t_eval))
        sol = solve_ivp(self._deriv, t_span, y0, t_eval=t_eval, args=(self.params.beta, self.params.gamma, self.params.alpha))
        return sol.y * N
