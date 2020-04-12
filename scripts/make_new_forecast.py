import logging
import pandas as pd
import os.path as op
import pickle
from collections import defaultdict
from datetime import datetime
from models import SIRtParams as Params
from models import SIRt as Model
from forecast import forecast_countries, extract_cssegi_forecast_info
import scripts.config as config

logger = logging.getLogger(__name__)

N_DAYS_PREDICT = 400
COUNTRIES = ['Denmark', 'Iran', 'Spain', 'Italy', 'Sweden']
SEED = 43
DEFAULT_PARAMS = Params(I0=1e-6, R0=1e-6)


def main():
    out_time_series_folder = config.FORECAST_TS_DIR
    out_info_folder = config.FORECAST_INFO_DIR
    data_file = config.CSSEGI_PREPROC_DATA_FILE

    logger.info('Calculating new forecast ...')

    df_all = pd.read_pickle(data_file)

    start_params = defaultdict(lambda: DEFAULT_PARAMS)
    start_params['Denmark'] = Params(I0=1e-12, R0=1e-12)
    start_params['Spain'] = Params(I0=1e-11, R0=1e-11)
    start_params['Italy'] = Params(I0=1e-11, R0=1e-11)

    df_forecasts, forecast_info_collection = forecast_countries(
        df_all,
        col_country='country',
        model_class=Model,
        extract_forecast_info=extract_cssegi_forecast_info,
        n_days_predict=N_DAYS_PREDICT,
        start_params_collection=start_params,
        countries=COUNTRIES,
        seed=SEED
    )
    update_time = datetime.now().strftime('%Y-%m-%d')

    forecast_file_path = op.join(out_time_series_folder, update_time + '.pickle')
    with open(forecast_file_path, 'wb') as forecast_file:
        pd.to_pickle(df_forecasts, forecast_file)

    forecast_infos_file_path = op.join(out_info_folder, update_time + '.pickle')
    with open(forecast_infos_file_path, 'wb') as forecast_info_file:
        pickle.dump(forecast_info_collection, forecast_info_file)
    logger.info(f'New forecast marked with date {update_time} saved in {out_time_series_folder}.')

    return update_time


if __name__ == '__main__':
    main()
