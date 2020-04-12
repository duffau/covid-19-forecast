from typing import Iterable, Sequence
from datetime import datetime
from pandas import DataFrame, Series
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from forecast import ForecastInfo


def plot_forecast(df_forecast: DataFrame, forecast_info: ForecastInfo, days_short_term=5, days_long_term=30) -> plt.Figure:
    fig = plt.figure(figsize=(8, 5), constrained_layout=True)
    gs = fig.add_gridspec(4, 3)
    long_term_plot = fig.add_subplot(gs[0:2, 0:2])
    beta_plot = fig.add_subplot(gs[2:4, 0:2])
    stat_box_1 = fig.add_subplot(gs[0, 2])
    stat_box_2 = fig.add_subplot(gs[1, 2])
    stat_box_3 = fig.add_subplot(gs[2, 2])
    stat_box_4 = fig.add_subplot(gs[3, 2])

    stats = calc_plot_stats(df_forecast, forecast_info)
    r0 = stats['r0']
    peak_infected = stats['peak_infected']
    peak_date = stats['peak_date']

    fig.suptitle(df_forecast.country.iloc[0])

    make_centered_text_box(stat_box_1, f'Peak date:\n {peak_date.strftime("%d-%m-%Y")}')
    make_centered_text_box(stat_box_2, f'Peak number of infected:\n {format_counts(peak_infected)}')
    # make_centered_text_box(stat_box_3, f'Basic reproducion number\n$R_0 = {r0:.2g}$')
    # make_centered_text_box(stat_box_4, f'Current reproducion number\n$R_t = {rt:.2g}$')

    today = np.datetime64('now')
    short_term_mask = df_forecast.dates < today + np.timedelta64(days_short_term, 'D')
    long_term_mask = df_forecast.dates < today + np.timedelta64(days_long_term, 'D')

    make_infected_removed_plot(
        long_term_plot,
        dates=df_forecast.dates[long_term_mask],
        infected_forecast=df_forecast.infected_forecast[long_term_mask],
        infected_obs=df_forecast.infected_obs[long_term_mask],
        title=f'Forecasting {days_long_term} days ahead.'
    )

    make_beta_plot(
        beta_plot,
        dates=Series(forecast_info.beta_dates),
        beta_t=Series(forecast_info.beta_t),
        title=f'Estimated transmission rate - Transmissions per infected per day.'
    )

    return fig


def make_infected_removed_plot(ax, dates: Iterable[datetime],
                               infected_forecast: Sequence[float] = None,
                               removed_forecast: Sequence[float] = None,
                               infected_obs: Sequence[float] = None,
                               removed_obs: Sequence[float] = None,
                               title='', title_size=10,
                               ylabel="Persons",
                               date_formatter=DateFormatter("%d-%b")):
    ax.set_title(title, fontdict={'fontsize': title_size})

    if infected_forecast is not None:
        ax.plot(dates, infected_forecast, label="Infected - forecast")
    if removed_forecast is not None:
        ax.plot(dates, removed_forecast, label="Removed (Recovered + Dead)")
    if infected_obs is not None:
        ax.plot(dates, infected_obs, "k.:", label="Infected - Observed")
    if removed_obs is not None:
        ax.plot(dates, removed_obs, "k.:", label="Removed - Observed")

    ax.xaxis.set_major_formatter(date_formatter)
    ax.tick_params(axis='x', rotation=25)
    ax.grid("True")
    ax.set_ylabel(ylabel)
    ax.legend()
    return ax


def make_beta_plot(ax, dates: Sequence[datetime],
                   beta_t: Sequence[float],
                   title='', title_size=10,
                   ylabel="Persons per day",
                   date_formatter=DateFormatter("%d-%b")):
    ax.set_title(title, fontdict={'fontsize': title_size})

    ax.plot(dates, beta_t, label="Avg. transmission rate (beta)")
    ax.xaxis.set_major_formatter(date_formatter)
    ax.tick_params(axis='x', rotation=25)
    ax.grid("True")
    ax.set_ylabel(ylabel)
    ax.legend()
    return ax


def make_centered_text_box(ax, textstr, size=11):
    ax.text(0.5, 0.5, textstr, size=size, ha="center", va="center")
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    return ax


def calc_plot_stats(df_forecast: DataFrame, forecast_info: ForecastInfo) -> dict:
    peak_infected_index = df_forecast.infected_forecast.idxmax()
    try:
        r0 = forecast_info.params.beta / forecast_info.params.gamma
    except AttributeError:
        r0 = forecast_info.beta_t / forecast_info.params.gamma

    return {
        'r0': r0,
        'peak_infected': df_forecast.infected_forecast[peak_infected_index],
        'peak_date': df_forecast.dates[peak_infected_index]
    }


def format_counts(count):
    if count < 1e5:
        return f'{count:.0f}'
    elif count < 1e6:
        return f'{count / 1e3:.0f} Thousand'
    elif count < 1e9:
        return f'{count / 1e6:.2f} Million'
    else:
        return f'{count / 1e9:.2f} Billion'


def save_plot(fig: plt.Figure, filename: str) -> None:
    fig.savefig(filename)


if __name__ == '__main__':
    import pandas as pd

    # countries = ['Denmark', 'Spain', 'Iran', 'Italy', 'Sweden']
    df_forecast = pd.read_pickle('../data/forecasts/time_series/2020-03-20.pickle')
    forecast_info_collection = pd.read_pickle('../data/forecasts/info/2020-03-20.pickle')
    for country in df_forecast.country.unique():
        print(f'Plotting {country}')
        df_plot = df_forecast[df_forecast.country == country].copy()
        forecast_info = forecast_info_collection.get(country)
        fig = plot_forecast(df_plot, forecast_info)
        save_plot(fig, f'../forecast_plots/{country.lower()}_{forecast_info.model_name}.png')
