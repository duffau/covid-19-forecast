from typing import Iterable
from datetime import datetime
from pandas import DataFrame

from models import SIRParams


class ForecastInfo:

    def __init__(self, id: str, model_name: str, forecast_time: datetime, latest_data_point: datetime, params: SIRParams):
        self.id = id
        self.model_name = model_name
        self.forecast_time = forecast_time
        self.latest_data_point = latest_data_point
        self.params = params

    def __str__(self):
        sorted_attributes = sorted(self.__dict__.items(), key=lambda item: item[0])
        public_attributes = [(k, v) for k, v in sorted_attributes if not k.startswith('_')]
        return '\n'.join([f'{k} = "{v}"' for k, v in public_attributes])

    def to_ini(self):
        header = "[forecast-info]"
        body = str(self)
        return "\n".join([header, body])


class ForecastInfoCollection:
    def __init__(self):
        self.collection = {}

    def add(self, forecast_info: ForecastInfo):
        self.collection[forecast_info.id] = forecast_info

    def get(self, id):
        return self.collection.get(id)


def extract_cssegi_forecast_info(country: str, model_name: str, params: SIRParams, df: DataFrame):
    return ForecastInfo(
        id=country,
        model_name=model_name,
        forecast_time=datetime.now(),
        latest_data_point=df.date.max().to_pydatetime(),
        params=params
    )

