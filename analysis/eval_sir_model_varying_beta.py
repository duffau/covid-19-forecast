import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
import math
from scipy.integrate import solve_ivp
from scipy.optimize import minimize
from collections import namedtuple

pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 1000)
PLOT_FOLDER = 'plots/var_beta'
DATA_FILE = '../data/pre-processed/cssegi_sand_data/cssegi_agg_data.pickle'
plot_filename = 'var_beta.png'

n_steps = 50
x = np.linspace(0, 16*math.pi, n_steps)
BETA = (np.sin(x) + 1)
print(x)
print(BETA)
GAMMA = 1/2.9
R0 = BETA/GAMMA
S_0 = 1
I_0 = 0.01
R_0 = 0
t_min = 0
t_max = 20
t_eval = np.linspace(t_min, t_max, num=n_steps)
t_span = min(t_eval), max(t_eval)
I_t = I_0*np.exp((R0-1)*GAMMA*t_eval)
S_t = S_0 - I_t
R_t = 0
y_obs = S_t, I_t, R_t
gamma = GAMMA


def beta(t):
    float_index = (t-t_min)/(t_max - t_min)*(n_steps-1)
    return BETA[np.int(float_index)]


def sir_deriv(t, y, beta, gamma):
    S, I, R = y
    dSdt = -beta(t) * S * I
    dIdt = beta(t) * S * I - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt


def eval_sir_model(beta, gamma, I_0, S_0, R_0, t_span, t_eval=None):
    y0 = (S_0, I_0, R_0)
    # print(f'beta = {beta}, gamma = {gamma}, R0 = {R0}, S0 = {S0}, I0 = {I0}')
    sol = solve_ivp(sir_deriv, t_span, y0, t_eval=t_eval, args=(beta, gamma))
    return sol.y


def sum_sq(y_obs, beta, gamma, I_0, S_0, R_0, t_span, t_eval=None):
    S_hat_t, I_hat_t, R_hat_t = eval_sir_model(beta, gamma, I_0, S_0, R_0, t_span, t_eval=t_eval)
    S_t, I_t, R_t = y_obs
    val = 0
    val += ((S_hat_t - S_t)**2).mean()
    val += ((I_hat_t - I_t)**2).mean()
    val += ((R_hat_t - R_t)**2).mean()
    # print('sumsq:', val)
    return val

def minimize_wrapper(params):
    beta, R0, I0 = inv_repam(params)
    return sum_sq(y_obs, beta, gamma, I_0, S_0, R_0, t_span, t_eval)

def inv_repam(params):
    return np.exp(params)

def repam(params):
    return np.log(params)



# res = minimize(
#     minimize_wrapper, np.array(fit_params),
#     method='Nelder-Mead',
#     options={'maxiter': 2500, 'maxfev': 5000}
# )
# print(res)
# beta, R0, I0 = inv_repam(res.x)

print(f'beta = {beta}, gamma = {gamma}, R_0 = {R_0}, S_0 = {S_0}, I_0 = {I_0}')
S_t, I_t, R_t = eval_sir_model(beta, gamma, I_0, S_0,  R_0, t_span, t_eval)

fig = plt.figure(figsize=(8, 5))
plt.plot(t_eval, S_t, label="Susceptible")
plt.plot(t_eval, I_t, label=f"Infectious")
plt.plot(t_eval, R_t, label=f"Removed")
param_string = f'R_0 = {beta(0)/gamma:.2f}\nbeta= {beta(0):.3g}\ngamma = {gamma:.3g}' #Susceptible_0 = {S_0:.3g} Infected_0 = {I_0:.3g} Removed_0 = {R_0:.3g}'
plt.text(0.01, .5, param_string, ha='left', va='top', transform=plt.gca().transAxes)
plt.xticks(rotation=45)
plt.grid("True")
plt.legend()
plt.savefig(os.path.join(PLOT_FOLDER, plot_filename))
plt.close()

plt.plot(t_eval, [beta(t) for t in t_eval], label="Beta")
plt.savefig(os.path.join(PLOT_FOLDER, 'beta_t.png'))
