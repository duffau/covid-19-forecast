import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os.path as op
import os

import statsmodels.api as sm

pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 1000)
PLOT_FOLDER = 'plots/beta_regr'
DATA_FILE = '../data/pre-processed/cssegi_sand_data/cssegi_agg_data.pickle'
PLOT_NAME = 'beta_regr'
GEO_REGION_VAR = 'country'
INFECTIOUS_PERIOD = 2.9
GAMMA = 1 / INFECTIOUS_PERIOD
LOWESS_FRAC = 0.5

os.makedirs(PLOT_FOLDER, exist_ok=True)

df_all = pd.read_pickle(DATA_FILE)
df_all['log_total_infected'] = np.log(df_all['total_infected'])

country = 'Denmark'
plot_filename = f'{country}_{PLOT_NAME}.png'.lower()

df = df_all[df_all.country == country]
x_var = 'dates'
y_var = 'log_total_infected'

df_fit = df[['date', 'total_infected', y_var]].replace([np.inf, -np.inf], np.nan).dropna()
dates_obs = pd.to_datetime(df_fit.date).values
y_obs = df_fit[y_var].values

SECS_PER_DAY = 60 * 60 * 24
days_since_start = (dates_obs - dates_obs[0]).astype('timedelta64[s]').astype('float64') / SECS_PER_DAY
ols_fit = sm.OLS(endog=y_obs, exog=sm.add_constant(days_since_start)).fit()
print(ols_fit.summary())
print(f'ols_fit.params: {ols_fit.params}')
ols_slope = ols_fit.params[1]

lowess_fit = sm.nonparametric.lowess(endog=y_obs, exog=days_since_start, frac=LOWESS_FRAC, return_sorted=False)
df_fit['lowess_fit'] = lowess_fit
df_fit['lowess_fit_exp'] = np.exp(lowess_fit)


def end_slope(x, lowess_fit, n_end=5):
    return ((lowess_fit[-1] - lowess_fit[-1 - n_end]) / (x[-1] - x[-1 - n_end]))


def beta(slope, gamma):
    return (slope / gamma + 1) * gamma


lowess_slope = end_slope(days_since_start, lowess_fit, n_end=5)
print(f'lowes end slope: {lowess_slope}')

beta_hat_lin_reg = beta(ols_slope, GAMMA)
print(f'beta_hat lin reg = {beta_hat_lin_reg}')
beta_hat_lowess = beta(lowess_slope, GAMMA)
print(f'beta_hat lowess = {beta_hat_lowess}')

ax = df_fit.plot(x='date', y=['total_infected', 'lowess_fit_exp'], logy=True, title=country)
ax.set_ylabel('infected - log scale')
plt.savefig(op.join(PLOT_FOLDER, plot_filename))
