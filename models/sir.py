from typing import Iterable
from models.params import SIRParams
from scipy.integrate import solve_ivp


class SIR:

    def __init__(self, params: SIRParams):
        self.params = params

    def fit(self, y_obs):
        pass

    def _deriv(self, t, y, beta, gamma):
        S, I, R = y
        dSdt = -beta * S * I
        dIdt = beta * S * I - gamma * I
        dRdt = gamma * I
        return dSdt, dIdt, dRdt

    def simulate(self, t_eval: Iterable[float]):
        y0 = (self.params.S0, self.params.I0, self.params.R0)
        t_span = (min(t_eval), max(t_eval))
        sol = solve_ivp(self._deriv, t_span, y0, t_eval=t_eval, args=(self.params.beta, self.params.gamma))
        return sol.y
