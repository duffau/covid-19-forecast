from typing import Iterable
import pandas as pd
import numpy as np
import random
import logging
from scipy.integrate import solve_ivp
from scipy.optimize import minimize
from . import Params
from forecast.forecast_info import ForecastInfo, ForecastInfoCollection


logger = logging.getLogger(__name__)


def forecast_countries(df: pd.DataFrame,
                       col_country: str,
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

        df_forecast, forecast_info = forecast(df_country, country, extract_forecast_info, n_days_predict, start_params, seed)
        df_forecasts.append(df_forecast)
        forecast_info_col.add(forecast_info)
    return pd.concat(df_forecasts, axis=0, ignore_index=True), forecast_info_col


def forecast(df, country, extract_forecast_info: callable, n_days_predict: int,
             start_params=None, seed=42) -> (pd.DataFrame, ForecastInfo):
    SCALING = 1000
    GAMMA = 1/2.9
    MODEL_NAME = 'SIR'

    logger.info(f"Forecasting {country}")
    df = df[df.country == country]
    if df.size < 2:
        return None, None
    try:
        dates_obs = pd.to_datetime(df.date).values
    except AttributeError:
        dates_obs = pd.to_datetime(df.last_update_date).values

    susceptible_obs = df.total_susceptible.values / SCALING
    infected_obs = df.total_infected.values / SCALING
    removed_obs = df.total_removed.values / SCALING
    N = df.population.iloc[0] / SCALING
    y_obs = susceptible_obs, infected_obs, removed_obs
    logger.info(f'N: {N}')

    def sir_deriv(t, y, N, beta, gamma):
        S, I, R = y
        dSdt = -beta * S * I / N
        dIdt = beta * S * I / N - gamma * I
        dRdt = gamma * I
        return dSdt, dIdt, dRdt

    def eval_sir_model(beta, gamma, I0, S0, R0, N, t_span, t_eval=None):
        y0 = (S0, I0, R0)
        logger.debug(f'beta: {beta}, gamma: {gamma}, S0: {S0}, I0: {I0}')
        sol = solve_ivp(sir_deriv, t_span, y0, t_eval=t_eval, args=(N, beta, gamma))
        return sol.y

    def sum_sq(y_obs, beta, gamma, I0, S0, R0, N, t_span, t_eval=None):
        S_hat_t, I_hat_t, R_hat_t = eval_sir_model(beta, gamma, I0, S0, R0, N, t_span, t_eval=t_eval)
        S_t, I_t, R_t = y_obs
        val = 0
        val += ((S_hat_t - S_t) ** 2).mean()
        val += ((I_hat_t - I_t) ** 2).mean()
        val += ((R_hat_t - R_t) ** 2).mean()
        logger.debug(f'sumsq: {val:.3g}')
        return val

    def minimize_wrapper(params):
        beta, R0, I0 = inv_repam(params)
        return sum_sq(y_obs, beta, gamma, I0, S0, R0, N, t_span, t_eval=t_eval)

    def inv_repam(params):
        return np.exp(params)

    def repam(params):
        return np.log(params)

    if start_params:
        beta, R0, I0 = start_params.beta, start_params.R0, start_params.I0
    else:
        random.seed(seed)
        beta = random.uniform(0.01, 5.0)
        I0 = infected_obs[0] if infected_obs[0] > 0 else random.uniform(a=1.0 / SCALING, b=50.0 / SCALING)
        R0 = removed_obs[0] if removed_obs[0] > 0 else random.uniform(a=1.0 / SCALING, b=50.0 / SCALING)

    fit_params = repam([beta, R0, I0])

    gamma = GAMMA
    S0 = susceptible_obs[0]

    dates_pred = np.arange(dates_obs[-1] + np.timedelta64(1, 'D'), dates_obs[-1] + np.timedelta64(n_days_predict + 1, 'D'), np.timedelta64(1, 'D'))
    dates_eval_pred = np.append(dates_obs, dates_pred)

    SECS_PER_DAY = 60 * 60 * 24
    t_eval = (dates_obs - dates_obs[0]).astype('timedelta64[s]').astype('float64') / SECS_PER_DAY
    t_eval_pred = (dates_eval_pred - dates_eval_pred[0]).astype('timedelta64[s]').astype('float64') / SECS_PER_DAY
    t_span = (t_eval_pred.min(), t_eval_pred.max())

    res = minimize(
        minimize_wrapper, np.array(fit_params),
        method='Nelder-Mead',
        options={'maxiter': 2500, 'maxfev': 5000}
    )
    logger.info(res)
    beta, R0, I0 = inv_repam(res.x)
    logger.info(f'R0 = {beta / gamma:.2f}')
    logger.info(f'beta = {beta:.3g}, gamma = {gamma:.3g}, S0 = {S0:.3g}, I0 = {I0:.3g}, R0 = {R0:.3g}')

    S_t, I_t, R_t = eval_sir_model(beta, gamma, I0, S0, R0, N, t_span, t_eval_pred)

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
                                          model_name=MODEL_NAME,
                                          df=df,
                                          params=Params(beta=beta, gamma=gamma, I0=I0, R0=R0, S0=S0)
                                          )
    return df_forecast, forecast_info
