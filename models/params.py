import numpy as np


class Params:

    @property
    def values(self) -> np.ndarray:
        raise NotImplementedError

    @classmethod
    def from_values(cls, values):
        raise NotImplementedError

    @classmethod
    def from_random(cls, seed):
        raise NotImplementedError

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False

        for atr in self.__dict__.keys():
            if not atr.startswith('_'):
                if not self.__dict__[atr] == other.__dict__[atr]:
                    return False
        return True


class SIRParams(Params):

    def __init__(self, beta=None, gamma=None, S0=None, I0=None, R0=None):
        self.beta = beta
        self.gamma = gamma
        self.S0 = S0
        self.I0 = I0
        self.R0 = R0

    def __repr__(self):
        return f'SIRParams(beta={self.beta}, gamma={self.gamma}, S0={self.S0}, I0={self.I0}, R0={self.R0})'

    @property
    def values(self) -> np.ndarray:
        return np.array([self.beta, self.gamma, self.S0, self.I0, self.R0])

    @classmethod
    def from_values(cls, values):
        return cls(*values)

    @classmethod
    def from_random(cls, seed=42):
        np.random.seed(seed)
        rand = np.random.random(size=(5,))
        rand *= np.array((1., 1., 0.1, 0.1, 0.1))
        rand += np.array((0., 0., 0.9, 0.0, 0.0))
        return cls.from_values(rand)


class SEIRParams(Params):

    def __init__(self, beta=None, gamma=None, alpha=None, S0=None, E0=None, I0=None, R0=None):
        self.beta = beta
        self.gamma = gamma
        self.alpha = alpha
        self.S0 = S0
        self.E0 = E0
        self.I0 = I0
        self.R0 = R0

    def __repr__(self):
        return f'SIRParams(beta={self.beta}, gamma={self.gamma}, alpha={self.alpha}, S0={self.S0}, E0={self.E0}, I0={self.I0}, R0={self.R0})'

    @property
    def values(self) -> np.ndarray:
        return np.array([self.beta, self.gamma, self.alpha, self.S0, self.E0, self.I0, self.R0])

    @classmethod
    def from_values(cls, values):
        return cls(*values)

    @classmethod
    def from_random(cls, seed=42):
        np.random.seed(seed)
        rand = np.random.random(size=(7,))
        rand *= np.array((1., 1., 1., 0.1, 0.1, 0.1, 0.1))
        rand += np.array((0., 0., 0., 0.9, 0.0, 0.0, 0.0))
        return cls.from_values(rand)
