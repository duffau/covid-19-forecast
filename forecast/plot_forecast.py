from typing import Iterable, Sequence
from datetime import datetime
from pandas import DataFrame, Series
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.dates import DateFormatter
from forecast import ForecastInfo
from utils import uri

COLORS = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00', '#ffff33', '#a65628', '#f781bf', '#999999']


def plot_forecast(df_forecast: DataFrame, forecast_info: ForecastInfo, days_long_term=30) -> plt.Figure:
    fig = plt.figure(figsize=(7, 5), constrained_layout=True)
    gs = fig.add_gridspec(5, 2)
    stat_box_1 = fig.add_subplot(gs[0, 0])
    stat_box_2 = fig.add_subplot(gs[0, 1])
    infected_plot = fig.add_subplot(gs[1:, 0:])

    stats = calc_plot_stats(df_forecast, forecast_info)
    peak_infected = stats['peak_infected']
    peak_date = stats['peak_date']

    fig.suptitle(df_forecast.country.iloc[0])

    make_centered_text_box(stat_box_1, f'Peak date:\n {format_date(peak_date)}')
    make_centered_text_box(stat_box_2, f'Peak number of infected:\n {format_counts_long(peak_infected)}')

    today = np.datetime64('now')
    long_term_mask = df_forecast.dates < today + np.timedelta64(days_long_term, 'D')

    make_infected_removed_plot(
        infected_plot,
        dates=df_forecast.dates[long_term_mask],
        infected_forecast=df_forecast.infected_forecast[long_term_mask],
        infected_obs=df_forecast.infected_obs[long_term_mask],
        title=f'Forecasting {days_long_term} days ahead.'
    )

    return fig


def make_infected_removed_plot(ax, dates: Iterable[datetime],
                               infected_forecast: Sequence[float] = None,
                               removed_forecast: Sequence[float] = None,
                               infected_obs: Sequence[float] = None,
                               removed_obs: Sequence[float] = None,
                               title='', title_size=10,
                               ylabel="Persons",
                               yticks_formatter=ticker.FuncFormatter(lambda x, pos: format_counts_short(x)),
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

    ax.yaxis.set_major_formatter(yticks_formatter)
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


def make_r0_plot(ax,
                 r0_t: Sequence[float],
                 dates: Sequence[datetime],
                 dates_obs: Sequence[datetime],
                 title='', title_size=10,
                 ylabel="Transmissions per day",
                 date_formatter=DateFormatter("%d-%b")):
    ax.set_title(title, fontdict={'fontsize': title_size})

    r0_obs = np.array(r0_t)
    r0_obs[~np.isin(dates, dates_obs)] = np.nan

    r0_fct = np.array(r0_t)
    r0_fct[np.isin(dates, dates_obs)] = np.nan
    ax.plot(dates, r0_obs, color=COLORS[1], label="$R_0$")
    ax.plot(dates, r0_fct, color=COLORS[1], linestyle='dashed', label="$R_0$ - forecast")
    ax.xaxis.set_major_formatter(date_formatter)
    ax.tick_params(axis='x', rotation=25)
    ax.grid("True")
    ax.set_ylabel(ylabel)
    ax.legend()
    return ax


def calc_plot_stats(df_forecast: DataFrame, forecast_info: ForecastInfo) -> dict:
    try:
        try:
            r0 = forecast_info.params.beta / forecast_info.params.gamma
        except AttributeError:
            r0 = forecast_info.beta_t / forecast_info.params.gamma
    except Exception:
        r0 = np.full(shape=df_forecast.infected_forecast.shape, fill_value=np.nan)
    try:
        peak_infected_index = df_forecast.infected_forecast.idxmax()
        peak_infected = df_forecast.infected_forecast[peak_infected_index]
        peak_date = df_forecast.dates[peak_infected_index]
    except Exception:
        peak_infected = np.nan
        peak_date = None

    return {
        'r0': r0,
        'peak_infected': peak_infected,
        'peak_date': peak_date
    }


def format_date(date):
    if date is not None:
        return date.strftime("%d-%m-%Y")
    else:
        return 'NA'


def format_counts_long(count):
    if count is not None:
        if count < 1e5:
            return format(int(count), ',')
        elif count < 1e6:
            return f'{count / 1e3:.0f} Thousand'
        elif count < 1e9:
            return f'{count / 1e6:.2f} Million'
        else:
            return f'{count / 1e9:.2f} Billion'
    else:
        return 'NA'


def format_counts_short(count):
    if count < 1e3:
        return format(int(count), ',')
    elif count < 1e6:
        return f'{count / 1e3:.1f}K'
    elif count < 1e9:
        return f'{count / 1e6:.1f}M'
    else:
        return f'{count / 1e9:.1f}B'


def save_plot(fig: plt.Figure, filename: str) -> None:
    fig.savefig(filename)
    fig.clf()
    plt.close()


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
        save_plot(fig, f'../forecast_plots/{uri.clean(country.lower())}_{forecast_info.model_name}.png')
