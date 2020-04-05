import pytest
from models import SIRParams, SIR
import numpy as np

BETA = 0.6
GAMMA = 0.35
N = 1.0
I0 = 0.001
S0 = N - I0
R0 = 0.0


@pytest.fixture
def sir_params():
    params = SIRParams(
        beta=BETA,
        gamma=GAMMA,
        S0=S0,
        I0=I0,
        R0=R0
    )
    return params


@pytest.fixture
def sir_model(sir_params):
    model = SIR(params=sir_params)
    return model


@pytest.fixture
def sir_sim(model):
    t_eval = range(50)
    return model.simulate(t_eval=t_eval)


def test_init_sir_params(sir_params):
    pass


def test_equal_params():
    params1 = SIRParams(beta=BETA, gamma=GAMMA, S0=S0, I0=I0, R0=R0)
    params2 = SIRParams(beta=BETA, gamma=GAMMA, S0=S0, I0=I0, R0=R0)
    assert params1 == params2


def test_not_equal_params():
    params1 = SIRParams(beta=BETA, gamma=GAMMA, S0=S0, I0=I0, R0=R0)
    params2 = SIRParams(beta=BETA + 1, gamma=GAMMA, S0=S0, I0=I0, R0=R0)
    assert params1 != params2


def test_params_values(sir_params):
    vals = sir_params.values
    expected_vals = np.array([BETA, GAMMA, S0, I0, R0])
    assert (vals == expected_vals).all()


def test_init_model(sir_model):
    pass


def test_simulate_model(sir_model):
    n = 50
    t_eval = range(n)
    S, I, R = sir_model.simulate(t_eval=t_eval)
    assert len(S) == n
    assert len(I) == n
    assert len(R) == n

    assert ((S >= 0) & (S <= 1)).all()
    assert ((I >= 0) & (I <= 1)).all()
    assert ((R >= 0) & (R <= 1)).all()

    assert (S > 0).any()
    assert (I > 0).any()
    assert (R > 0).any()

    assert ((S + I + R) - N < 1e-15).all()
