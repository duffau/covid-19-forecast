from typing import Iterable
from .params import Params


class Model:

    def __init__(self, params: Params):
        self.params = params

    @property
    def name(self):
        return self.__class__.__name__

    def fit(self, y_obs, t_eval):
        raise NotImplementedError

    def simulate(self, t_eval: Iterable[float], N=1.0):
        raise NotImplementedError
