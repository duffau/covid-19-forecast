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


def test_equal_params():
    params1 = SEIRParams(beta=BETA, gamma=GAMMA, alpha=ALPHA, S0=S0, E0=E0, I0=I0, R0=R0)
    params2 = SEIRParams(beta=BETA, gamma=GAMMA, alpha=ALPHA, S0=S0, E0=E0, I0=I0, R0=R0)
    assert params1 == params2


def test_not_equal_params():
    params1 = SEIRParams(beta=BETA, gamma=GAMMA, alpha=ALPHA, S0=S0, E0=E0, I0=I0, R0=R0)
    params2 = SEIRParams(beta=BETA + 1, gamma=GAMMA, alpha=ALPHA, S0=S0, E0=E0, I0=I0, R0=R0)
    assert params1 != params2


def test_params_values(seir_params):
    vals = seir_params.values
    expected_vals = np.array([BETA, GAMMA, ALPHA, S0, E0, I0, R0])
    assert (vals == expected_vals).all()


def test_params_from_values(seir_params):
    vals = seir_params.values
    new_params = SEIRParams.from_values(vals)
    assert new_params == seir_params


def test_params_from_random():
    new_params = SEIRParams.from_random(seed=123)
    assert new_params.beta > 0.0
    assert new_params.beta < 1.0

    assert new_params.gamma > 0.0
    assert new_params.gamma < 1.0

    assert new_params.alpha > 0.0
    assert new_params.alpha < 1.0

    assert new_params.S0 > 0.9
    assert new_params.S0 < 1.0

    assert new_params.E0 > 0.0
    assert new_params.E0 < 0.1

    assert new_params.I0 > 0.0
    assert new_params.I0 < 0.1

    assert new_params.R0 > 0.0
    assert new_params.R0 < 0.1


def test_init_model(seir_model):
    pass


def test_model_name(seir_model):
    assert seir_model.name == 'SEIR'


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

    assert (np.abs((S + E + I + R) - N) < 1e-15).all()


def test_fit_model(seir_model):
    n = 50
    xatol = 1e-5
    fatol = 1e-5
    t_eval = range(n)
    y_obs = seir_model.simulate(t_eval=t_eval)
    start_params = SEIRParams.from_random(seed=1234)
    start_params.gamma = GAMMA
    start_params.alpha = ALPHA
    start_params.S0 = S0
    new_model = SEIR(params=start_params)
    new_model.fit(y_obs, t_eval, options={'xatol': xatol, 'fatol': fatol})
    assert (np.abs(new_model.params.values - seir_model.params.values) < 0.01).all()
