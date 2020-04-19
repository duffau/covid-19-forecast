import os
import glob
import logging
import scripts.config as config

logger = logging.getLogger(__name__)


FORECAST_PLOT_FOLDER = config.FORECAST_PLOT_FOLDER

logger.info('Deleting all forecast plots ...')
forecast_plots_paths = glob.glob(os.path.join(FORECAST_PLOT_FOLDER, '*.png'))
forecast_info_paths = glob.glob(os.path.join(FORECAST_PLOT_FOLDER, '*.ini'))

for png_file, ini_file in zip(forecast_plots_paths, forecast_info_paths):
    os.remove(png_file)
    os.remove(ini_file)


