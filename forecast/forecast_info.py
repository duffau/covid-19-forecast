from datetime import datetime
from pandas import DataFrame


class ForecastInfo:

    def __init__(self, id: str, model_name: str, forecast_time: datetime, latest_data_point: datetime):
        self.id = id
        self.model_name = model_name
        self.forecast_time = forecast_time
        self.latest_data_point = latest_data_point

    def __str__(self):
        sorted_attributes = sorted(self.__dict__.items(), key=lambda item: item[0])
        public_attributes = [(k, v) for k, v in sorted_attributes if not k.startswith('_')]
        return '\n'.join([f'{k} = "{v}"' for k, v in public_attributes])

    def to_ini(self):
        header = "[forecast-info]"
        body = str(self)
        return "\n".join([header, body])


def extract_cssegi_forecast_info(country: str, model_name: str, df: DataFrame):
    return ForecastInfo(
        id=country,
        model_name=model_name,
        forecast_time=datetime.now(),
        latest_data_point=df.date.max().to_pydatetime()
    )


if __name__ == '__main__':
    fi = ForecastInfo(
        id='some string',
        model_name='SIR',
        forecast_time=datetime(2020, 3, 19, 17, 59),
        latest_data_point=datetime(2020, 3, 18, 12, 0)
    )
    print(str(fi))
