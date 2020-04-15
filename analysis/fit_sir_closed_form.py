import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import minimize

pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 1000)
PLOT_FOLDER = 'plots/forecasts'
DATA_FILE = '../data/pre-processed/cssegi_sand_data/cssegi_agg_data.pickle'

country = 'Italy'
df_all = pd.read_pickle(DATA_FILE)
df = df_all[df_all.country == country]
N = df.population.iloc[0]
infected_obs = df.total_infected.values/N
t_obs = np.array(range(len(infected_obs)))

start_params_collection = {
    'China': [2.65194937e-01,8.42629781e-02,1.01377756e-04,1.62245063e-06,1.63972157e-07]
}

def i_t_Shabbir_et_al(t, beta, gamma, S0, I0):
    c = S0 + I0 - 1
    lamda = beta - gamma + beta * c
    d = (lamda - I0 * beta) / lamda * I0 * np.exp(beta * c / gamma)
    return lamda / (beta + lamda * d * np.exp(-lamda * t) * np.exp(beta * c / gamma))


def sum_sq_Shabbir_et_al(t, infected_obs, beta, gamma, S0, I0):
    I_hat_t = i_t_Shabbir_et_al(t, beta, gamma, S0, I0)
    val = 0
    val += ((I_hat_t - infected_obs) ** 2).mean()
    print('sumsq:', val)
    return val


def i_t_Bohner_et_al(t, b, c, S0=0.99, I0=0.01, t0=0):
    kappa = I0 / S0
    i_t = I0 * (1 + kappa) ** (b / (b - c))
    i_t *= (1 + kappa * np.exp((b - c) * (t - t0))) ** (-b / (b - c))
    i_t *= np.exp((b - c) * (t - t0))
    return i_t


def sum_sq_Bohner_et_al(t, infected_obs, b, c, S0=0.99, I0=0.01, t0=0):
    I_hat_t = i_t_Bohner_et_al(t, b, c, S0, I0, t0)
    val = 0
    val += ((I_hat_t - infected_obs) ** 2).mean()
    print('sumsq:', val)
    return val


def minimize_wrapper(params):
    params = inv_repam(params)
    return sum_sq_Bohner_et_al(t, infected_obs, *params)


def inv_repam(params):
    return np.exp(params)


def repam(params):
    return np.log(params)


i_t = i_t_Bohner_et_al

# t = np.array(range(100))
# It = i_t(t, 0.2, 0.1, 0.999999, 0.000001, 0)
# plt.plot(t, It)
# plt.plot(t_obs, infected_obs)
# plt.show()
i0 = max(infected_obs)*0.1
rand_scale = np.array([0.01, 0.01, 0.0001, 0.0001, 1])*1
start_params = np.array([0.7, 0.55, 0.005, i0, 5]) + (np.random.random(size=5)*2 - 1)*rand_scale
start_params = start_params_collection.get(country, start_params)
fit_params = repam(start_params)

t = np.array(range(100))
It = i_t(t, *start_params)
# plt.plot(t, It, label='start params')
plt.plot(t_obs, infected_obs,'o-', label='obs')

# fit_params = repam(np.random.random(size=5))
t = t_obs
res = minimize(
    minimize_wrapper, np.array(fit_params),
    method='Nelder-Mead',
    options={'gtol': 1e-14}
)
print(res)
print(inv_repam(res.x))

It = i_t(t, *inv_repam(res.x))
plt.plot(t_obs, It, label='fitted params')
plt.title(f'Infected - {country}')
plt.ylabel('Pct. of population')
plt.xlabel('Days')
plt.legend()
plt.savefig(f'plots/closed_form/sir_{country}.png')
plt.close()
