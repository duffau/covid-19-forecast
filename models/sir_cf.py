from typing import Iterable
from .model import Model
from .params import SIRCFParams
from .utils import *

from scipy.integrate import solve_ivp
from scipy.optimize import minimize
import numpy as np


class SIRClosedForm(Model):
    FIT_PARAMS_UPPER = np.array([5.0, 5.0, 1.0, 1.0, 300])
    FIT_PARAMS_LOWER = np.array([0.0, 0.0, 0.0, 0.0, -300])

    def __init__(self, params: SIRCFParams=None, seed=42):
        if not params:
            params = SIRCFParams.from_random(seed=seed)
        super().__init__(params)

    def fit(self, y_obs, t_eval, options=None):

        _options = {'gtol': 1e-24}
        if options:
            _options.update(options)

        res = minimize(
            fun=self._minimize_wrapper,
            x0=self.free_params,
            args=(y_obs, t_eval),
            method='BFGS',
            options=_options
        )
        print(res)

    @property
    def free_params(self):
        param_lower = self.FIT_PARAMS_LOWER
        param_upper = self.FIT_PARAMS_UPPER
        selected_params = np.array([self.params.b, self.params.c, self.params.S0, self.params.I0, self.params.t0])
        return self.repam(selected_params, param_lower, param_upper)

    def _minimize_wrapper(self, free_params, y_obs, t_eval):
        # print(f'fit_params: {fit_params}')
        param_lower = self.FIT_PARAMS_LOWER
        param_upper = self.FIT_PARAMS_UPPER
        b, c, S0, I0, t0 = self.inv_repam(free_params, param_lower, param_upper)
        # print(f'beta, R0, I0: {beta, R0, I0}')
        R0 = None
        self._update_params(b, c, S0, I0, R0, t0)
        return self._sum_sq(y_obs, t_eval)

    def inv_repam(self, free_params, lower, upper):
        return sigmoid(free_params, lower, upper)

    def repam(self, free_params, lower, upper):
        return inv_sigmoid(free_params, lower, upper)

    def _sum_sq(self, y_obs, t_eval):
        S_hat_t, I_hat_t, R_hat_t = self.simulate(t_eval=t_eval)
        S_t, I_t, R_t = y_obs
        val = 0
        val += ((I_hat_t - I_t) ** 2).mean()
        # print(f'sum_sq: {val}')
        return val

    def _update_params(self, b, c, S0, I0, R0, t0):
        if b is not None:
            self.params.b = b

        if c is not None:
            self.params.c = c

        if S0 is not None:
            self.params.S0 = S0

        if I0 is not None:
            self.params.I0 = I0

        if R0 is not None:
            self.params.R0 = R0

        if t0 is not None:
            self.params.t0 = t0

    def simulate(self, t_eval: Iterable[float], N=1.0):
        b, c, S0, I0, R0, t0 = self.params.values
        kappa = I0 / S0
        i_t = I0 * (1 + kappa) ** (b / (b - c))
        i_t *= (1 + kappa * np.exp((b - c) * (t_eval - t0))) ** (-b / (b - c))
        i_t *= np.exp((b - c) * (t_eval - t0))
        return np.full(i_t.shape, np.nan), i_t*N, np.full(i_t.shape, np.nan)

