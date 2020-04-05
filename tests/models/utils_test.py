import numpy as np
import math
import models.utils as ut


def test_sigmoid():
    x = np.array([-1, 0, 1])
    y_expected = np.array([1/(1 + math.e), 0.5, math.e/(math.e + 1)])
    y = ut.sigmoid(x)
    assert (y == y_expected).all()


def test_inv_sigmoid():
    x = np.array([-1, 0, 1])
    x_out = ut.inv_sigmoid(ut.sigmoid(x))
    assert (x == x_out).all()