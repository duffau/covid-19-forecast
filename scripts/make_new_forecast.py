import logging
import pandas as pd
import os.path as op
import pickle
from datetime import datetime
from models import SIRClosedForm as Model
from forecast import forecast_countries, extract_cssegi_forecast_info
import scripts.config as config

logger = logging.getLogger(__name__)



def main():
    out_time_series_folder = config.FORECAST_TS_DIR
    out_info_folder = config.FORECAST_INFO_DIR
    data_file = config.CSSEGI_PREPROC_DATA_FILE
    start_params = config.START_PARAMS
    n_days_predict = config.N_DAYS_PREDICT
    countries = config.COUNTRIES
    skip_countries = config.SKIP_COUNTRIES
    seed = config.SEED

    logger.info('Calculating new forecast ...')

    df_all = pd.read_pickle(data_file)

    df_forecasts, forecast_info_collection = forecast_countries(
        df_all,
        col_country='country',
        model_class=Model,
        extract_forecast_info=extract_cssegi_forecast_info,
        n_days_predict=n_days_predict,
        start_params_collection=start_params,
        skip_countries=skip_countries,
        countries=countries,
        seed=seed
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
