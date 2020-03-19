from forecast.forecast_info import ForecastInfo, extract_cssegi_forecast_info
from datetime import datetime
from pandas import DataFrame


def test_forecast_info_init():
    ForecastInfo(
        id='some string',
        forecast_time=datetime(2020, 3, 19, 17, 59),
        latest_data_point=datetime(2020, 3, 18, 12, 0)
    )


def test_extract_cssegi_forecast_info_datetime():
    max_date = datetime(2020, 3, 18, 12, 00)
    df = DataFrame({'date': [datetime(2020, 3, 15, 18, 00), max_date]})
    fc_info = extract_cssegi_forecast_info('Denmark', df)
    assert fc_info.latest_data_point == max_date
    assert isinstance(fc_info.forecast_time, datetime)
