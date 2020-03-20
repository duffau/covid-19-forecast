import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
from scipy.integrate import solve_ivp
from scipy.optimize import minimize
from collections import namedtuple

pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 1000)
PLOT_FOLDER = '../forecast_plots'
DATA_FILE = '../data/pre-processed/cssegi_sand_data/cssegi_agg_data.csv'
RANDOM_SEED = 43
df_all = pd.read_csv(DATA_FILE)
model_name = 'sir'
Params = namedtuple('Params', ['beta', 'gamma', 'I0'])

t0 = 0
n_days_predict = 10
# N = 120000
start_params = {
    # 'China': Params(beta=0.06138, gamma=0.046619, I0=2.02930572e+04, S0=1000000),
    'China': Params(beta=0.35,
                    gamma=0.04,
                    I0=200)
}

# for country in ['China', 'Denmark', 'Iran', 'Sweden', 'Italy', 'Spain']:
for country in ['China']:
    plot_filename = f'{country}_{model_name}.png'.lower()

    df = df_all[df_all.country == country]
    # df.info()
    print(f"Forecasting {country}")
    # print(df)
    if df.size < 2:
        continue
    try:
        dates_obs = pd.to_datetime(df.date).values
    except AttributeError:
        dates_obs = pd.to_datetime(df.last_update_date).values

    susceptible_obs = df.total_susceptible.values
    infected_obs = df.total_infected.values
    removed_obs = df.total_removed.values
    y_obs = susceptible_obs, infected_obs, removed_obs
    N = df.population.iloc[0]*1000
    print(f'N: {N}')

    def sir_deriv(t, y, N, beta, gamma):
        S, I, R = y
        dSdt = -beta * S * I / N
        dIdt = beta * S * I / N - gamma * I
        dRdt = gamma * I
        return dSdt, dIdt, dRdt


    def eval_sir_model(beta, gamma, I0, S0, R0, N, t_span, t_eval=None):
        y0 = (S0, I0, R0)
        print(f'beta: {beta}, gamma: {gamma}, S0: {S0}, I0: {I0}')
        sol = solve_ivp(sir_deriv, t_span, y0, t_eval=t_eval, args=(N, beta, gamma))
        return sol.y


    def sum_sq(y_obs, beta, gamma, I0, S0, R0, N, t_span, t_eval=None):
        S_hat_t, I_hat_t, R_hat_t = eval_sir_model(beta, gamma, I0, S0, R0, N, t_span, t_eval=t_eval)
        S_t, I_t, R_t = y_obs
        val = 0
        # val += ((S_hat_t - S_t)**2).mean()
        val += ((I_hat_t - I_t)**2).mean()
        # val += ((R_hat_t - R_t)**2).mean()
        print('sumsq:', val)
        return val

    def minimize_wrapper(params, y_obs, t_eval, *args, **kwargs):
        beta, gamma, I0 = inv_repam(params)
        return sum_sq(y_obs, beta, gamma, I0, t_eval=t_eval, *args, **kwargs)

    def inv_repam(params):
        return np.exp(params)

    def repam(params):
        return np.log(params)


    if country in start_params:
        beta, gamma, I0 = repam(start_params[country])
        # beta, gamma, I0, S0 = start_params[country]
    else:
        np.random.seed(RANDOM_SEED)
        beta, gamma = np.random.uniform(low=0.01, high=5.0, size=2)
        I0 = infected_obs[0] if infected_obs[0] > 0 else random.uniform(a=1.0, b=50.0, size=1)
        S0 = random.uniform(a=susceptible_obs[0]*0.1, b=susceptible_obs[0])
        print([beta, gamma, I0, S0])
        beta, gamma, I0, S0 = repam([beta, gamma, I0, S0])


    S0 = susceptible_obs[0]
    R0 = removed_obs[0]

    dates_pred = np.arange(dates_obs[-1] + np.timedelta64(1, 'D'), dates_obs[-1] + np.timedelta64(n_days_predict+1, 'D'), np.timedelta64(1, 'D'))
    dates_eval_pred = np.append(dates_obs, dates_pred)

    SECS_PER_DAY = 60*60*24
    t_eval = (dates_obs - dates_obs[0]).astype('timedelta64[s]').astype('float64')/SECS_PER_DAY
    t_eval_pred = (dates_eval_pred - dates_eval_pred[0]).astype('timedelta64[s]').astype('float64')/SECS_PER_DAY
    t_span = (min(t0, t_eval_pred.min()), t_eval_pred.max())

    print("t_eval:", t_eval)
    print("t_eval_pred:", t_eval_pred)
    res = minimize(
        minimize_wrapper, np.array([beta, gamma, I0]), (y_obs, t_eval, S0, R0, N, t_span),
        method='Nelder-Mead',
        options={'maxiter': 2500, 'maxfev': 5000}
    )
    print(res)
    beta, gamma, I0 = inv_repam(res.x)
    print(f'R0 = {beta/gamma:.2f}')
    S_t, I_t, R_t = eval_sir_model(beta, gamma, I0, S0,  R0, N, t_span, t_eval_pred)


    fig = plt.figure(figsize=(8, 5))
    # plt.plot(dates_eval_pred, S_t, label="Susceptible")
    plt.plot(dates_eval_pred, I_t, label="Infected")
    plt.plot(dates_eval_pred, R_t, label="Removed (Dead + Immune)")
    # plt.plot(dates_obs, susceptible_obs, "k*:", label="Susceptible - Observed")
    plt.plot(dates_obs, infected_obs, "k*:", label="Infected - Observed")
    plt.plot(dates_obs, removed_obs, "k*:", label="Removed - Observed")
    plt.xticks(rotation=45)
    plt.grid("True")
    plt.title(country)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(PLOT_FOLDER, plot_filename))
