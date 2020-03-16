import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import minimize

pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 1000)
PLOT_FOLDER = '../forecast_plots'
DATA_FILE = '../data/pre-processed/historical/nssac_agg_data.pickle'
df_all = pd.read_pickle(DATA_FILE)
model_name = 'sir'

for country in ['Denmark', 'Iran', 'Sweden', 'Italy', 'Spain']:
    plot_filename = f'{country}_{model_name}.png'.lower()

    df = df_all[df_all.country == country]
    df.info()
    print(f"Forecasting {country}")
    print(df)
    if df.size < 2:
        continue

    dates_obs = df.date.values
    susceptible_obs = df.total_susceptible.values
    infected_obs = df.total_infected.values
    removed_obs = df.total_removed.values
    y_obs = susceptible_obs, infected_obs, removed_obs
    N = df.population.iloc[0]
    n_days_predict = 5

    def sir_deriv(t, y, N, beta, gamma):
        S, I, R = y
        dSdt = -beta * S * I / N
        dIdt = beta * S * I / N - gamma * I
        dRdt = gamma * I
        return dSdt, dIdt, dRdt


    def eval_sir_model(params, t_span, y0, N, t_eval=None):
        beta, gamma = params
        sol = solve_ivp(sir_deriv, t_span, y0, t_eval=t_eval, args=(N, beta, gamma))
        return sol.y


    def sum_sq(params, y_obs, t_eval, *args, **kwargs):
        y_pred = eval_sir_model(params, t_eval=t_eval, *args, **kwargs)
        return sum(((y_o - y_p)**2).sum() for y_o, y_p in zip(y_obs, y_pred))


    beta, gamma = [.45, 0.1]
    y0 = (susceptible_obs[0], infected_obs[0], removed_obs[0])

    dates_pred = np.arange(dates_obs[-1] + np.timedelta64(1, 'D'), dates_obs[-1] + np.timedelta64(n_days_predict+1, 'D'), np.timedelta64(1, 'D'))
    dates_eval_pred = np.append(dates_obs, dates_pred)

    SECS_PER_DAY = 60*60*24
    t_eval = (dates_obs - dates_obs[0]).astype('timedelta64[s]').astype('float64')/SECS_PER_DAY
    t_eval_pred = (dates_eval_pred - dates_eval_pred[0]).astype('timedelta64[s]').astype('float64')/SECS_PER_DAY
    t_span = (t_eval_pred.min(), t_eval_pred.max())

    print("t_eval:", t_eval)
    res = minimize(
        sum_sq, np.array([beta, gamma]), (y_obs, t_eval, t_span, y0, N),
        method='Nelder-Mead'
    )
    print(res)

    beta, gamma = res.x
    y_eval = eval_sir_model((beta, gamma), t_span, y0, N, t_eval_pred)
    S_t, I_t, R_t = y_eval


    fig = plt.figure(figsize=(8, 5))
    # plt.plot(dates_eval_pred, S_t, label="Susceptible")
    plt.plot(dates_eval_pred, I_t, label="Infected")
    plt.plot(dates_eval_pred, R_t, label="Removed (Dead + Immune)")
    plt.plot(dates_obs, infected_obs, "k*:", label="Infected - Observed")
    plt.plot(dates_obs, removed_obs, "k*:", label="Removed - Observed")
    plt.xticks(rotation=45)
    plt.grid("True")
    plt.title(country)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(PLOT_FOLDER, plot_filename))
