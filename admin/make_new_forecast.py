import logging
import pandas as pd
import os.path as op
import pickle
from datetime import datetime
from forecast import forecast_countries, Params, extract_cssegi_forecast_info, plot_forecast, save_plot


def main():
    OUT_TIME_SERIES_FOLDER = '../data/forecasts/time_series'
    OUT_INFO_FOLDER = '../data/forecasts/info'
    DATA_FILE = '../data/pre-processed/cssegi_sand_data/cssegi_agg_data.pickle'
    N_DAYS_PREDICT = 400
    COUNTRIES = ['Denmark', 'Spain', 'Iran', 'Italy', 'Sweden']
    SEED = 42

    df_all = pd.read_pickle(DATA_FILE)

    logging.basicConfig(level=logging.INFO)

    start_params = {
        'Denmark': Params(beta=1.4863183028145124, gamma=0.9927890258623339, I0=1e-7),
        # 'China': StartParams(beta=0.35, gamma=0.04, I0=200)
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

    forecast_file_path = op.join(OUT_TIME_SERIES_FOLDER, update_time + '.pickle')
    with open(forecast_file_path, 'wb') as forecast_file:
        pd.to_pickle(df_forecasts, forecast_file)

    forecast_infos_file_path = op.join(OUT_INFO_FOLDER, update_time + '.pickle')
    with open(forecast_infos_file_path, 'wb') as forecast_info_file:
        pickle.dump(forecast_info_collection, forecast_info_file)

    return update_time

if __name__ == '__main__':
    main()
