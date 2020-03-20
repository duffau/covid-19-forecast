from pandas import DataFrame
import matplotlib.pyplot as plt


def plot_forecast(df_forecast: DataFrame) -> plt.Figure:
    fig = plt.figure(figsize=(8, 5))
    return fig


def calc_plot_stats(df_forecast) -> dict:
    return {'x': 1.2, 'y': 3.4}


def save_plot(fig: plt.Figure, filename: str) -> None:
    fig.savefig(filename)
