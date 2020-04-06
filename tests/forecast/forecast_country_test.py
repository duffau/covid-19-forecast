import pytest

from models import SIRParams, SIR
from forecast.forecast_country import forecast
from forecast import extract_cssegi_forecast_info
import pandas as pd
from datetime import datetime

COUNTRY = 'Country'
N_POP = 1e6
N = 1.0
BETA = 0.6
GAMMA = 0.35
I0 = 0.001
R0 = 0.0
S0 = N - I0 - R0

@pytest.fixture
def sir_model():
    params = SIRParams(
        beta=BETA,
        gamma=GAMMA,
        S0=S0,
        I0=I0,
        R0=R0
    )
    return SIR(params=params)

@pytest.fixture
def df(sir_model):
    n = 50
    S, I, R = sir_model.simulate(t_eval=range(n), N=N_POP)
    return pd.DataFrame({
        'date': pd.date_range(datetime.today(), periods=n),
        'country': [COUNTRY]*n,
        'population': [N_POP]*n,
        'total_susceptible': S,
        'total_infected': I,
        'total_removed': R
    })


def test_forecast(df, sir_model, mocker):
    sir_model.fit = mocker.Mock(spec_set=sir_model.fit)
    df_forecast, forecast_info = forecast(
        df=df,
        country=COUNTRY,
        model=sir_model,
        extract_forecast_info=extract_cssegi_forecast_info,
        n_days_predict=10
    )

