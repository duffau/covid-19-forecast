class Params:
    pass


class SIRParams(Params):

    def __init__(self, beta=None, gamma=None, S0=None, I0=None, R0=None):
        self.beta = beta
        self.gamma = gamma
        self.S0 = S0
        self.I0 = I0
        self.R0 = R0


class SEIRParams(Params):

    def __init__(self, beta=None, gamma=None, alpha=None, S0=None, E0=None ,I0=None, R0=None):
        self.beta = beta
        self.gamma = gamma
        self.alpha = alpha
        self.S0 = S0
        self.E0 = E0
        self.I0 = I0
        self.R0 = R0
