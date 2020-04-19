"""
Inspired by Boner et al (2018) application of their dynamic SIR model
result in equation (10).
"""
import numpy as np
import scipy.interpolate as itrp
import matplotlib.pyplot as plt


def infected(t, b: callable, c: callable, s0, i0, t0):
    prod = np.exp(np.cumsum(np.log(1 + c(t) - b(t)) + np.log(1 + g(t, b, c, s0, i0, t0))))
    return i0 / prod


def g(ts, b: callable, c: callable, s0, i0, t0):
    # _ts = np.arange(t0, max(ts))
    kappa = i0 / s0
    _num = b(ts) * kappa
    _denom = np.exp(np.cumsum(np.log(1 + c(ts) - b(ts)))) + kappa * (1 + c(ts) - b(ts))
    return _num / _denom


def b(t, params):
    # TODO: Implement np.itrp() Spline to be able to fit to data.
    # return np.full(t.shape, B)
    return (np.sin(t)+1)/2 * B

def c(t):
    return (np.cos(t)+1)/2 * C


B = 0.9
C = 0.8
t0 = 0
i0 = 0.01
s0 = 1 - i0
t = np.arange(t0, 50)
it = infected(t, b, c, s0, i0, t0)
plt.plot(t, it)
plt.savefig(f'plots/closed_form/varying_params.png')
