import pytest
from models import SEIR, SEIRParams
import numpy as np

BETA = 0.6
GAMMA = 0.35
ALPHA = 0.15
N = 1.0
E0 = 0
I0 = 0.01
S0 = N - I0 - E0
R0 = 0.0


@pytest.fixture
def seir_params():
    params = SEIRParams(
        beta=BETA,
        gamma=GAMMA,
        alpha=ALPHA,
        S0=S0,
        E0=E0,
        I0=I0,
        R0=R0
    )
    return params


@pytest.fixture
def seir_model(seir_params):
    model = SEIR(params=seir_params)
    return model


def test_init_params(seir_params):
    pass


def test_params_values(seir_params):
    vals = seir_params.values
    expected_vals = np.array([BETA, GAMMA, ALPHA, S0, E0, I0, R0])
    assert (vals == expected_vals).all()


def test_init_model(seir_model):
    pass


def test_simulate_model(seir_model):
    n = 50
    t_eval = range(n)
    S, E, I, R = seir_model.simulate(t_eval=t_eval)
    assert len(S) == n
    assert len(I) == n
    assert len(R) == n

    assert ((S >= 0) & (S <= 1)).all()
    assert ((E >= 0) & (E <= 1)).all()
    assert ((I >= 0) & (I <= 1)).all()
    assert ((R >= 0) & (R <= 1)).all()

    assert (S > 0).any()
    assert (E > 0).any()
    assert (I > 0).any()
    assert (R > 0).any()

    assert ((S + E + I + R) - N < 1e-15).all()
