from typing import Iterable
from .params import SEIRParams
from scipy.integrate import solve_ivp


class SEIR:

    def __init__(self, params: SEIRParams):
        self.params = params

    def fit(self, y_obs):
        pass

    def _deriv(self, t, y, beta, gamma, alpha):
        S, E, I, R = y
        dSdt = -beta * S * I
        dEdt = beta * S * I - alpha * I
        dIdt = alpha * E - gamma * I
        dRdt = gamma * I
        return dSdt, dEdt, dIdt, dRdt

    def simulate(self, t_eval: Iterable[float]):
        y0 = (self.params.S0, self.params.E0, self.params.I0, self.params.R0)
        t_span = (min(t_eval), max(t_eval))
        sol = solve_ivp(self._deriv, t_span, y0, t_eval=t_eval, args=(self.params.beta, self.params.gamma, self.params.alpha))
        return sol.y
