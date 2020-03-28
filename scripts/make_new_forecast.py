import logging
import pandas as pd
import os.path as op
import pickle
from datetime import datetime
from models import SIRParams as Params
from forecast import forecast_countries, extract_cssegi_forecast_info
import scripts.config as config

logger = logging.getLogger(__name__)

N_DAYS_PREDICT = 400
COUNTRIES = ['Denmark', 'Spain', 'Italy', 'Sweden']
SEED = 42


def main():
    out_time_series_folder = config.FORECAST_TS_DIR
    out_info_folder = config.FORECAST_INFO_DIR
    data_file = config.CSSEGI_PREPROC_DATA_FILE

    logger.info('Calculating new forecast ...')

    df_all = pd.read_pickle(data_file)

    start_params = {
        'Denmark': Params(beta=1.4863183028145124, gamma=None, R0=0.1, I0=1e-7, S0=None),
    }

    df_forecasts, forecast_info_collection = forecast_countries(
        df_all,
        col_country='country',
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
