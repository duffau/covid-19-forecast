import pytest
from forecast.forecast_info import ForecastInfo, extract_cssegi_forecast_info
from datetime import datetime
from pandas import DataFrame
from models import SIRParams


def test_forecast_info_init():
    ForecastInfo(
        id='some string',
        model_name='SIR',
        forecast_time=datetime(2020, 3, 19, 17, 59),
        latest_data_point=datetime(2020, 3, 18, 12, 0),
        params=SIRParams(),
    )


@pytest.fixture
def fc_info():
    return ForecastInfo(
        id='some string',
        model_name='SIR',
        forecast_time=datetime(2020, 3, 19, 17, 59),
        latest_data_point=datetime(2020, 3, 18, 12, 0),
        params=SIRParams()
    )


def test_forecast_info_str(fc_info):
    assert str(fc_info)


def test_forecast_info_ini_format(fc_info):
    config_str = fc_info.to_ini()
    lines = config_str.split('\n')
    n_attr = 8
    assert len(lines) == n_attr + 1


def test_extract_cssegi_forecast_info_datetime():
    max_date = datetime(2020, 3, 18, 12, 00)
    beta_t = [0.5, 0.6, 0.7]
    beta_dates = [datetime(2020, 3, 8, 00, 00), datetime(2020, 3, 10, 18, 00), datetime(2020, 3, 11, 18, 00)]
    beta_obs_dates = [datetime(2020, 3, 10, 18, 00), datetime(2020, 3, 11, 18, 00)]
    df = DataFrame({'date': [datetime(2020, 3, 15, 18, 00), max_date]})
    params = SIRParams()
    fc_info = extract_cssegi_forecast_info(
        country='Denmark',
        model_name='The Model',
        params=params,
        beta_t=beta_t,
        beta_dates=beta_dates,
        beta_obs_dates=beta_obs_dates,
        df=df
    )
    assert fc_info.latest_data_point == max_date
    assert isinstance(fc_info.forecast_time, datetime)
