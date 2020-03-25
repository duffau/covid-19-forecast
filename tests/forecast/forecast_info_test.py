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
        params=SIRParams()
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
    n_attr = 5
    assert len(lines) == n_attr + 1


def test_extract_cssegi_forecast_info_datetime():
    max_date = datetime(2020, 3, 18, 12, 00)
    df = DataFrame({'date': [datetime(2020, 3, 15, 18, 00), max_date]})
    params = SIRParams()
    fc_info = extract_cssegi_forecast_info('Denmark', 'The Model', params, df)
    assert fc_info.latest_data_point == max_date
    assert isinstance(fc_info.forecast_time, datetime)
