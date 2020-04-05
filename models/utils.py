import numpy as np


def sigmoid(x, lower=0.0, upper=1.0):
    return np.where(x >= 0, 1 / (1 + np.exp(-x)), np.exp(x) / (1 + np.exp(x))) * (upper - lower) + lower


def inv_sigmoid(y, lower=0.0, upper=1.0):
    y = ((y - lower)/(upper - lower))
    return np.log(y) - np.log(1 - y)
