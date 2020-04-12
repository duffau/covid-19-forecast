import pytest

from models import SIRParams, SIR
from models import SIRtParams, SIRt
from forecast.forecast_country import forecast, ForecastInfo
from forecast import extract_cssegi_forecast_info
import pandas as pd
import numpy as np
from datetime import datetime

COUNTRY = 'Country'
N_POP = 1e6
N = 1.0
BETA = 0.6
GAMMA = 0.35
I0 = 0.001
R0 = 0.0
S0 = N - I0 - R0
N_T_EVAL = 50
N_PREDICT = 10
T = range(30)
BETA_T = np.interp(T, [0, 10], [0.65, 0.5])


def sir_model():
    params = SIRParams(
        beta=BETA,
        gamma=GAMMA,
        S0=S0,
        I0=I0,
        R0=R0
    )
    return SIR(params=params)



def sirt_model():
    params = SIRtParams(
        gamma=GAMMA,
        S0=S0,
        I0=I0,
        R0=R0
    )
    return SIRt(params=params, beta_t=BETA_T, t=T)


def df_sim(model):
    n = N_T_EVAL
    S, I, R = model.simulate(t_eval=range(n), N=N_POP)
    return pd.DataFrame({
        'date': pd.date_range(datetime.today(), periods=n),
        'country': [COUNTRY] * n,
        'population': [N_POP] * n,
        'total_susceptible': S,
        'total_infected': I,
        'total_removed': R
    })


def df_sir():
    return df_sim(sir_model())


def df_sirt():
    return df_sim(sirt_model())


@pytest.mark.parametrize("df,model", [(df_sir(), sir_model()), (df_sirt(), sirt_model())])
def test_forecast(df, model, mocker):
    model.fit = mocker.Mock(spec_set=model.fit)
    df_forecast, forecast_info = forecast(
        df=df,
        country=COUNTRY,
        model=model,
        extract_forecast_info=extract_cssegi_forecast_info,
        n_days_predict=N_PREDICT
    )
    assert isinstance(df_forecast, pd.DataFrame)
    assert df_forecast.shape[0] == N_T_EVAL + N_PREDICT
    assert isinstance(forecast_info, ForecastInfo)
