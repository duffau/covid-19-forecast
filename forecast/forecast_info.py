from datetime import datetime
from pandas import DataFrame


class ForecastInfo:

    def __init__(self, forecast_time: datetime, latest_data_point: datetime):
        self.forecast_time = forecast_time
        self.latest_data_point = latest_data_point

    def __str__(self):
        return f'forecast_time={self.forecast_time}\nlatest_data_point={self.latest_data_point}'


def extract_cssegi_forecast_info(df: DataFrame):
    return ForecastInfo(
        forecast_time=datetime.now(),
        latest_data_point=df.date.max().to_pydatetime()
    )
