import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import minimize

pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 1000)
PLOT_FOLDER = 'plots'
DATA_FILE = '../data/pre-processed/historical/nssac_agg_data.pickle'
country = 'Denmark'

df = pd.read_pickle(DATA_FILE)
df = df[df.country == country]
df.info()

susceptible_obs = df.total_susceptible.values
infected_obs = df.total_infected.values
removed_obs = df.total_removed.values
y_obs = susceptible_obs, infected_obs, removed_obs
N = df.population.iloc[0]


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

t_span = (0, len(infected_obs))
t_eval = np.arange(t_span[0], t_span[1])
print(sum_sq((beta, gamma), y_obs, t_eval, t_span, y0, N))
res = minimize(
    sum_sq, np.array([beta, gamma]), (y_obs, t_eval, t_span, y0, N),
    method='Nelder-Mead'
)
print(res)
beta, gamma = res.x

n_predict = 5
t_span = (0, len(infected_obs) + n_predict)
t_eval = np.arange(t_span[0], t_span[1])
y_eval = eval_sir_model((beta, gamma), t_span, y0, N, t_eval)
S_t, I_t, R_t = y_eval

fig = plt.figure(figsize=(8, 5))
# plt.plot(t_eval, S_t, label="Susceptible")
plt.plot(t_eval, I_t, label="Infected")
plt.plot(t_eval, R_t, label="Removed (Dead + Immune)")
plt.plot(np.arange(0, len(infected_obs)), infected_obs, "k*:", label="Infected - Observed")
plt.plot(np.arange(0, len(removed_obs)), removed_obs, "k*:", label="Removed - Observed")
plt.grid("True")
plt.title(country)
plt.legend()
plt.show()
