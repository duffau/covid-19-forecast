import pandas as pd
import os.path as op
from forecast import plot_forecast, save_plot

OUT_TIME_SERIES_FOLDER = '../data/forecasts/time_series'
OUT_INFO_FOLDER = '../data/forecasts/info'
OUT_PLOT_FOLDER = '../forecast_plots'


def plot_forcasts(forecast_date):
    df_forecasts = pd.read_pickle(op.join(OUT_TIME_SERIES_FOLDER, f'{forecast_date}.pickle'))
    forecast_info_collection = pd.read_pickle(op.join(OUT_INFO_FOLDER, f'{forecast_date}.pickle'))

    for country in df_forecasts.country.unique():
        print(f'Plotting {country}')
        df_plot = df_forecasts[df_forecasts.country == country].copy()
        forecast_info = forecast_info_collection.get(country)
        fig = plot_forecast(df_plot, forecast_info, days_short_term=5, days_long_term=120)
        basefilename = f'{country.lower()}_{forecast_info.model_name}'
        save_plot(fig, op.join(OUT_PLOT_FOLDER, basefilename + '.png'))
        with open(op.join(OUT_PLOT_FOLDER, basefilename + '.ini'), 'w') as ini_file:
            ini_file.write(forecast_info.to_ini())


if __name__ == '__main__':
    plot_forcasts('2020-03-21')