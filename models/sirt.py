from typing import Iterable, Sequence
from .model import Model
from .params import SIRtParams
from .utils import *

from scipy.integrate import solve_ivp
from scipy.optimize import minimize
import statsmodels.api as sm
import numpy as np
import logging

logger = logging.getLogger(__name__)


class SIRt(Model):
    """SIR model expecting a time varying beta for simulations"""
    FIT_PARAMS_LOWER = np.array([0.0, 0.0])
    FIT_PARAMS_UPPER = np.array([1.0, 1.0])

    def __init__(self, params: SIRtParams = None, beta_t: Sequence = tuple(), t: Sequence = tuple(), seed=42):
        assert len(beta_t) == len(t), f'beta_t and t must have the same length: len(beta_t) = {len(beta_t)} != len(t) = {len(t)}'
        self.beta_t = np.array(beta_t)
        self.t = np.array(t)
        if not params:
            params = SIRtParams.from_random(seed=seed)
        super().__init__(params)

    def fit(self, y_obs, t_eval, lowess_frac=0.5, options=None, verbose=False):
        if len(self.beta_t) == 0:
            logger.info('Fitting beta path ...')
            self.fit_beta(y_obs, t_eval, lowess_frac=lowess_frac)

        _options = {'maxiter': 2500, 'maxfev': 5000}
        if options:
            _options.update(options)

        logger.info('Fitting remaining free parameters ...')
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
        free_params = np.array([self.params.R0, self.params.I0])
        return self.repam(free_params, param_lower, param_upper)

    def beta(self, t):
        return np.interp(t, self.t, self.beta_t)

    def _filter_growth_path(self, y, t_eval):
        top_index = np.argmax(y)
        return y[0:top_index], t_eval[0:top_index]

    def fit_beta(self, y_obs, t_eval, lowess_frac=0.5):
        log_I_t = np.log(y_obs[1])
        _t_eval = np.array(t_eval)
        log_I_t, _t_eval = self._filter_growth_path(log_I_t, _t_eval)
        log_I_t_hat = sm.nonparametric.lowess(endog=log_I_t,
                                              exog=_t_eval,
                                              frac=lowess_frac,
                                              missing='drop',
                                              return_sorted=False)
        slopes = self._slopes(log_I_t_hat, _t_eval)
        gamma = self.params.gamma
        beta_t = (slopes / gamma + 1) * gamma
        t = _t_eval[1:]
        self.beta_t = beta_t[~np.isnan(beta_t)]
        self.t = t[~np.isnan(beta_t)]
        print(f'beta_t: {self.beta_t}')
        print(f't: {self.t}')

    def _slopes(self, y, t_eval):
        return np.diff(y) / np.diff(t_eval)

    def _minimize_wrapper(self, fit_params, y_obs, t_eval):
        # print(f'fit_params: {fit_params}')
        param_lower = self.FIT_PARAMS_LOWER
        param_upper = self.FIT_PARAMS_UPPER
        R0, I0 = self.inv_repam(fit_params, param_lower, param_upper)
        # print(f'R0, I0: {R0, I0}')
        gamma = None
        S0 = None
        self._update_params(gamma, I0, S0, R0)
        return self._sum_sq(y_obs, t_eval)

    def inv_repam(self, fit_params, lower, upper):
        return sigmoid(fit_params, lower, upper)

    def repam(self, fit_params, lower, upper):
        return inv_sigmoid(fit_params, lower, upper)

    def _sum_sq(self, y_obs, t_eval):
        S_hat_t, I_hat_t, R_hat_t = self.simulate(t_eval=t_eval)
        S_t, I_t, R_t = y_obs
        val = 0
        val += ((S_hat_t - S_t) ** 2).mean()
        val += ((I_hat_t - I_t) ** 2).mean()
        val += ((R_hat_t - R_t) ** 2).mean()
        # print(f'sum_sq: {val}')
        return val

    def _update_params(self, gamma, I0, S0, R0):
        if gamma is not None:
            self.params.gamma = gamma

        if I0 is not None:
            self.params.I0 = I0

        if S0 is not None:
            self.params.S0 = S0

        if R0 is not None:
            self.params.R0 = R0

    def _deriv(self, t, y, beta, gamma):
        S, I, R = y
        dSdt = -beta(t) * S * I
        dIdt = beta(t) * S * I - gamma * I
        dRdt = gamma * I
        return dSdt, dIdt, dRdt

    def simulate(self, t_eval: Iterable[float], N=1.0):
        y0 = (self.params.S0, self.params.I0, self.params.R0)
        t_span = (min(t_eval), max(t_eval))
        sol = solve_ivp(self._deriv, t_span, y0, args=(self.beta, self.params.gamma))
        S, I, R = sol.y * N
        return np.interp(t_eval, sol.t, S), np.interp(t_eval, sol.t, I), np.interp(t_eval, sol.t, R)
