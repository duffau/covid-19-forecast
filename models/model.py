from typing import Iterable
from .params import Params


class Model:

    def __init__(self, params: Params):
        self.params = params

    def fit(self, y_obs, t_eval):
        raise NotImplementedError

    def simulate(self, t_eval: Iterable[float]):
        raise NotImplementedError
