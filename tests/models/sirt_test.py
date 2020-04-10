import pytest
from models import SIRtParams, SIRt
import numpy as np

T = range(50)
BETA_T = np.interp(T, [0, 10], [0.65, 0.5])
GAMMA = 0.35
N = 1.0
I0 = 0.01
R0 = 0.001
S0 = N - I0 - R0



@pytest.fixture
def sirt_params():
    params = SIRtParams(
        gamma=GAMMA,
        S0=S0,
        I0=I0,
        R0=R0
    )
    return params


@pytest.fixture
def sirt_model(sirt_params):
    model = SIRt(params=sirt_params, beta_t=BETA_T, t=T)
    return model


def test_init_sir_params(sirt_params):
    pass


def test_equal_params():
    params1 = SIRtParams(gamma=GAMMA, S0=S0, I0=I0, R0=R0)
    params2 = SIRtParams(gamma=GAMMA, S0=S0, I0=I0, R0=R0)
    assert params1 == params2


def test_not_equal_params():
    params1 = SIRtParams(gamma=GAMMA, S0=S0, I0=I0, R0=R0)
    params2 = SIRtParams(gamma=GAMMA - 1, S0=S0, I0=I0, R0=R0)
    assert params1 != params2


def test_params_values(sirt_params):
    vals = sirt_params.values
    expected_vals = np.array([GAMMA, S0, I0, R0])
    assert (vals == expected_vals).all()


def test_params_from_values(sirt_params):
    vals = sirt_params.values
    new_params = SIRtParams.from_values(vals)
    assert new_params == sirt_params


def test_params_from_random():
    new_params = SIRtParams.from_random(seed=123)
    assert new_params.gamma > 0.0
    assert new_params.gamma < 1.0

    assert new_params.S0 > 0.9
    assert new_params.S0 < 1.0

    assert new_params.I0 > 0.0
    assert new_params.I0 < 0.1

    assert new_params.R0 > 0.0
    assert new_params.R0 < 0.1


def test_init_model(sirt_model):
    pass


def test_model_name(sirt_model):
    assert sirt_model.name == 'SIRt'


def test_simulate_model(sirt_model):
    n = 50
    t_eval = range(n)
    S, I, R = sirt_model.simulate(t_eval=t_eval)

    # import matplotlib.pyplot as plt
    # plt.plot(t_eval,S, label='S')
    # plt.plot(t_eval, I, label='I')
    # plt.plot(T, R, label='R')
    # plt.legend()
    # plt.show()

    assert len(S) == n
    assert len(I) == n
    assert len(R) == n

    assert ((S >= 0) & (S <= 1)).all()
    assert ((I >= 0) & (I <= 1)).all()
    assert ((R >= 0) & (R <= 1)).all()

    assert (S > 0).any()
    assert (I > 0).any()
    assert (R > 0).any()

    assert (np.abs((S + I + R) - N) < 1e-15).all()


def test_fit_model(sirt_model):
    n = 50
    xatol = 1e-3
    t_eval = range(n)
    y_obs = sirt_model.simulate(t_eval=t_eval)
    start_params = SIRtParams.from_random(seed=42)
    start_params.gamma = GAMMA
    start_params.S0 = S0
    new_model = SIRt(params=start_params, beta_t=BETA_T, t=T)
    new_model.fit(y_obs, t_eval, options={'xatol': xatol})
    assert (np.abs(new_model.params.values - sirt_model.params.values) < 0.01).all()


def test_fit_model_and_beta(sirt_model):
    n = 50
    xatol = 1e-3
    t_eval = range(n)
    y_obs = sirt_model.simulate(t_eval=t_eval)
    start_params = SIRtParams.from_random(seed=42)
    start_params.gamma = GAMMA
    start_params.S0 = S0
    new_model = SIRt(params=start_params)
    new_model.fit(y_obs, t_eval, lowess_frac=0.01, options={'xatol': xatol})
    assert (np.abs(new_model.beta(t_eval) - sirt_model.beta(t_eval)) < 1.0).all()
    assert (np.abs(new_model.params.values - sirt_model.params.values) < 0.5).all()
