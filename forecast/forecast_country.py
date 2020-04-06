from typing import Iterable
import pandas as pd
import numpy as np
import logging

from models import Model
from forecast.forecast_info import ForecastInfo, ForecastInfoCollection


logger = logging.getLogger(__name__)


def forecast_countries(df: pd.DataFrame,
                       col_country: str,
                       model_class,
                       extract_forecast_info: callable,
                       n_days_predict: int,
                       start_params_collection: dict = None,
                       countries: Iterable = tuple(),
                       skip_countries: Iterable = tuple(),
                       seed=42) -> (pd.DataFrame, ForecastInfoCollection):

    skip_countries = set(skip_countries)
    df_forecasts = []
    forecast_info_col = ForecastInfoCollection()
    countries = countries if countries else df[col_country].unique()

    for country in countries:
        if country in skip_countries:
            print(f"Skipping {country}")
            continue

        df_country = df[df[col_country] == country]
        if start_params_collection:
            start_params = start_params_collection.get(country)
        else:
            start_params = None
        model = model_class(params=start_params, seed=seed)
        df_forecast, forecast_info = forecast(df_country,
                                              country,
                                              model,
                                              extract_forecast_info,
                                              n_days_predict)
        df_forecasts.append(df_forecast)
        forecast_info_col.add(forecast_info)
    return pd.concat(df_forecasts, axis=0, ignore_index=True), forecast_info_col


def forecast(df,
             country,
             model: Model,
             extract_forecast_info: callable,
             n_days_predict: int) -> (pd.DataFrame, ForecastInfo):

    GAMMA = 1/2.9

    logger.info(f"Forecasting {country}")
    df = df[df.country == country]
    if df.size < 2:
        return None, None
    try:
        dates_obs = pd.to_datetime(df.date).values
    except AttributeError:
        dates_obs = pd.to_datetime(df.last_update_date).values

    N = df.population.iloc[0]
    susceptible_obs = df.total_susceptible.values / N
    infected_obs = df.total_infected.values / N
    removed_obs = df.total_removed.values / N
    y_obs = susceptible_obs, infected_obs, removed_obs
    logger.info(f'N: {N}')

    model.params.gamma = GAMMA
    model.params.S0 = susceptible_obs[0]

    dates_pred = np.arange(dates_obs[-1] + np.timedelta64(1, 'D'), dates_obs[-1] + np.timedelta64(n_days_predict + 1, 'D'), np.timedelta64(1, 'D'))
    dates_eval_pred = np.append(dates_obs, dates_pred)

    SECS_PER_DAY = 60 * 60 * 24
    t_eval = (dates_obs - dates_obs[0]).astype('timedelta64[s]').astype('float64') / SECS_PER_DAY

    model.fit(y_obs, t_eval)

    t_eval_pred = (dates_eval_pred - dates_eval_pred[0]).astype('timedelta64[s]').astype('float64') / SECS_PER_DAY

    beta, gamma, S0, I0, R0 = model.params.values
    logger.info(f'R0 = {beta / gamma:.2f}')
    logger.info(f'beta = {beta:.3g}, gamma = {gamma:.3g}, S0 = {S0:.3g}, I0 = {I0:.3g}, R0 = {R0:.3g}')

    S_t, I_t, R_t = model.simulate(t_eval=t_eval_pred)

    def pad_nan(obs_array, n_predicted):
        return np.pad(obs_array, (0, n_predicted), 'constant', constant_values=np.nan)

    forecast_data = {
        'country': country,
        'dates': dates_eval_pred,
        'susceptible_obs': pad_nan(susceptible_obs, n_days_predict),
        'susceptible_forecast': S_t,
        'infected_obs': pad_nan(infected_obs, n_days_predict),
        'infected_forecast': I_t,
        'removed_obs': pad_nan(removed_obs, n_days_predict),
        'removed_forecast': R_t
    }

    df_forecast = pd.DataFrame(forecast_data)
    forecast_info = extract_forecast_info(country=country,
                                          model_name=model.name,
                                          df=df,
                                          params=model.params)
    return df_forecast, forecast_info
