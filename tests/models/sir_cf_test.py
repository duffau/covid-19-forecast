import pytest
from models import SIRCFParams, SIRClosedForm
import numpy as np

B = 0.6
C = 0.35
N = 1.0
I0 = 0.01
R0 = 0.001
S0 = N - I0 - R0
T0 = 0


@pytest.fixture
def sir_cf_params():
    params = SIRCFParams(
        b=B,
        c=C,
        S0=S0,
        I0=I0,
        R0=R0,
        t0=T0
    )
    return params


@pytest.fixture
def sir_cf_model(sir_cf_params):
    model = SIRClosedForm(params=sir_cf_params)
    return model


def test_init_sir_params(sir_cf_params):
    pass


def test_equal_params():
    params1 = SIRCFParams(b=B, c=C, S0=S0, I0=I0, R0=R0, t0=T0)
    params2 = SIRCFParams(b=B, c=C, S0=S0, I0=I0, R0=R0, t0=T0)
    assert params1 == params2


def test_not_equal_params():
    params1 = SIRCFParams(b=B, c=C, S0=S0, I0=I0, R0=R0, t0=T0)
    params2 = SIRCFParams(b=B + 1, c=C, S0=S0, I0=I0, R0=R0, t0=T0)
    assert params1 != params2


def test_params_values(sir_cf_params):
    vals = sir_cf_params.values
    expected_vals = np.array([B, C, S0, I0, R0, T0])
    assert (vals == expected_vals).all()


def test_params_from_values(sir_cf_params):
    vals = sir_cf_params.values
    new_params = SIRCFParams.from_values(vals)
    assert new_params == sir_cf_params


def test_params_from_random():
    new_params = SIRCFParams.from_random(seed=123)
    assert new_params.b > 0.0
    assert new_params.b < 5.0

    assert new_params.c > 0.0
    assert new_params.c < 5.0

    assert new_params.S0 > 0.9
    assert new_params.S0 < 1.0

    assert new_params.I0 > 0.0
    assert new_params.I0 < 0.1

    assert new_params.R0 > 0.0
    assert new_params.R0 < 0.1

    assert new_params.t0 > 0.0
    assert new_params.t0 < 300


def test_init_model(sir_cf_model):
    assert isinstance(sir_cf_model, SIRClosedForm)


def test_model_name(sir_cf_model):
    assert sir_cf_model.name == 'SIRClosedForm'


def test_model_repr(sir_cf_model):
    assert isinstance(eval(sir_cf_model.__repr__()), SIRClosedForm)


def test_simulate_model(sir_cf_model):
    n = 50
    t_eval = range(n)
    S, I, R = sir_cf_model.simulate(t_eval=t_eval)
    assert len(S) == n
    assert len(I) == n
    assert len(R) == n

    assert ((I >= 0) & (I <= 1)).all()

    assert (I > 0).any()


def test_fit_model(sir_cf_model):
    n = 50
    xatol = 1e-3
    t_eval = range(n)
    y_obs = sir_cf_model.simulate(t_eval=t_eval)
    start_params = SIRCFParams.from_random(seed=1)
    new_model = SIRClosedForm(params=start_params)
    new_model.fit(y_obs, t_eval, options={'xatol': xatol})
    y_sim = new_model.simulate(t_eval)
    assert (np.abs(y_obs[1] - y_sim[1]) < 0.01).all()
