import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
from scipy.integrate import solve_ivp
from scipy.optimize import minimize
from collections import namedtuple
from analysis.params import Params

pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 1000)
PLOT_FOLDER = 'plots/forecasts'
DATA_FILE = '../data/pre-processed/cssegi_sand_data/cssegi_agg_data.pickle'
RANDOM_SEED = 41
SCALE_FACTOR = 1000
INCUBATION_PERIOD = 4.0
INFECTIOUS_PERIOD = 2.9
df_all = pd.read_pickle(DATA_FILE)
model_name = 'SEIR'

t0 = 0
n_days_predict = 5
start_params = {
    'Denmark': Params(beta=2./INFECTIOUS_PERIOD, E0=.001, R0=0.001, I0=0.001),
    'Iran': Params(beta=2. / INFECTIOUS_PERIOD, E0=.001, R0=0.001, I0=0.001),
    'Sweden': Params(beta=2. / INFECTIOUS_PERIOD, E0=.001, R0=0.001, I0=0.001),
    'Italy': Params(beta=2. / INFECTIOUS_PERIOD, E0=.001, R0=0.001, I0=0.001),
    'Spain': Params(beta=2. / INFECTIOUS_PERIOD, E0=.001, R0=0.001, I0=0.001)
}

countries = ['Austria','Denmark', 'Iran', 'Sweden', 'Italy', 'Spain']

for country in countries:
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

    population = df.population.iloc[0]
    N = 1.
    susceptible_obs = df.total_susceptible.values/population
    infected_obs = df.total_infected.values/population
    removed_obs = df.total_removed.values/population
    y_obs = susceptible_obs, infected_obs, removed_obs
    print(f'N: {N}')

    def seir_deriv(t, y, N, beta, gamma, alpha):
        S, E, I, R = y
        dSdt = -beta * S * I / N
        dEdt = beta * S * I / N - alpha * E
        dIdt = alpha*E - gamma * I
        dRdt = gamma * I
        return dSdt, dEdt, dIdt, dRdt


    def eval_seir_model(beta, gamma, alpha, S0, E0, I0, R0, N, t_span, t_eval=None):
        y0 = (S0, E0, I0, R0)
        print(f'beta = {beta}, gamma = {gamma}, alpha = {alpha}, S0 = {S0}, E0 = {E0}, I0 = {I0}, R0 = {R0}')
        sol = solve_ivp(seir_deriv, t_span, y0, t_eval=t_eval, args=(N, beta, gamma, alpha))
        return sol.y


    def sum_sq(y_obs, beta, gamma, alpha, S0, E0, I0, R0, N, t_span, t_eval=None):
        S_hat_t, E_hat_t, I_hat_t, R_hat_t = eval_seir_model(beta, gamma, alpha, S0, E0, I0, R0, N, t_span, t_eval=t_eval)
        S_t, I_t, R_t = y_obs
        val = 0
        val += ((S_hat_t - S_t)**2).mean()
        val += ((I_hat_t - I_t)**2).mean()
        val += ((R_hat_t - R_t)**2).mean()
        print('sumsq:', val)
        return val

    def minimize_wrapper(params):
        beta, E0, I0, R0 = inv_repam(params)
        return sum_sq(y_obs, beta, gamma, alpha, S0, E0, I0, R0, N, t_span, t_eval)

    def inv_repam(params):
        return np.exp(params)

    def repam(params):
        return np.log(params)


    beta = start_params.get(country, Params()).beta
    S0 = start_params.get(country, Params()).S0
    E0 = start_params.get(country, Params()).E0
    I0 = start_params.get(country, Params()).I0
    R0 = start_params.get(country, Params()).R0

    random.seed(RANDOM_SEED)
    if not beta:
        beta = random.uniform(a=0.01, b=1.)
    if not E0:
        E0 = random.uniform(a=0.001, b=1.)
    if not I0:
        I0 = infected_obs[0] if infected_obs[0] > 0 else random.uniform(a=0.001, b=1.)
    if not R0:
        R0 = removed_obs[0] if removed_obs[0] > 0 else random.uniform(a=0.001, b=1.)

    fit_params = repam([beta, E0, I0, R0])
    gamma = 1/INFECTIOUS_PERIOD
    alpha = 1/INCUBATION_PERIOD
    S0 = susceptible_obs[0]

    dates_pred = np.arange(dates_obs[-1] + np.timedelta64(1, 'D'), dates_obs[-1] + np.timedelta64(n_days_predict+1, 'D'), np.timedelta64(1, 'D'))
    dates_eval_pred = np.append(dates_obs, dates_pred)

    SECS_PER_DAY = 60*60*24
    t_eval = (dates_obs - dates_obs[0]).astype('timedelta64[s]').astype('float64')/SECS_PER_DAY
    t_eval_pred = (dates_eval_pred - dates_eval_pred[0]).astype('timedelta64[s]').astype('float64')/SECS_PER_DAY
    t_span = (min(t0, t_eval_pred.min()), t_eval_pred.max())

    print("t_eval:", t_eval)
    print("t_eval_pred:", t_eval_pred)
    res = minimize(
        minimize_wrapper, np.array(fit_params),
        method='Nelder-Mead',
        options={'maxiter': 2500, 'maxfev': 5000}
    )
    print(res)
    beta, E0, I0, R0 = inv_repam(res.x)
    print(f'R0 = {beta/gamma:.2f}')
    S_t, E_t, I_t, R_t = eval_seir_model(beta, gamma, alpha, S0, E0, I0,  R0, N, t_span, t_eval_pred)

    fig = plt.figure(figsize=(8, 5))
    # plt.plot(dates_eval_pred, S_t, label="Susceptible")
    plt.plot(dates_eval_pred, I_t, label=f"Infected")
    plt.plot(dates_eval_pred, R_t, label=f"Removed (Dead + Immune)")
    # plt.plot(dates_obs, susceptible_obs, "k*:", label="Susceptible - Observed ({SCALE_FACTOR} pers.)")
    plt.plot(dates_obs, infected_obs, "k*:", label=f"Infected - Observed")
    plt.plot(dates_obs, removed_obs, "k*:", label=f"Removed - Observed")
    param_string = f'$R_0 = {beta/gamma:.2f}$\n$\\beta= {beta:.3g}$, $\\gamma = {gamma:.3g}$\n$Susceptible_0 = {S0:.3g}$\n$Infected_0 = {I0:.3g}$\n$Removed_0 = {R0:.3g}$'
    plt.text(0.01, .5, param_string, ha='left', va='top', transform=plt.gca().transAxes)
    plt.xticks(rotation=45)
    plt.grid("True")
    plt.title(country)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(PLOT_FOLDER, plot_filename))
