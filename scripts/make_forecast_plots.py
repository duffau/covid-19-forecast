import pandas as pd
import os
import os.path as op
from forecast import plot_forecast, save_plot
import logging
from glob import glob
import pickle

logger = logging.getLogger(__name__)


def main():
    import scripts.config as config
    ts_folder = config.FORECAST_TS_DIR
    info_folder = config.FORECAST_INFO_DIR
    out_plot_folder = config.FORECAST_PLOT_FOLDER
    os.makedirs(out_plot_folder, exist_ok=True)

    file_paths = glob(op.join(ts_folder, '*.pickle'))
    latest_filename = op.basename(sorted(file_paths, reverse=True)[0])
    logger.info(f'Latest forecast file: {latest_filename}')

    df_forecasts = pd.read_pickle(op.join(ts_folder, latest_filename))
    with open(op.join(info_folder, latest_filename), 'rb') as info_file:
        forecast_info_collection = pickle.load(info_file)

    for country in df_forecasts.country.unique():
        logger.info(f'Plotting {country} ...')
        df_plot = df_forecasts[df_forecasts.country == country].copy()
        forecast_info = forecast_info_collection.get(country)
        fig = plot_forecast(df_plot, forecast_info, days_long_term=120)
        basefilename = f'{country.lower()}_{forecast_info.model_name}'
        save_plot(fig, op.join(out_plot_folder, basefilename + '.png'))
        with open(op.join(out_plot_folder, basefilename + '.ini'), 'w') as ini_file:
            ini_file.write(forecast_info.to_ini())


if __name__ == '__main__':
    main()