import pandas as pd
import matplotlib.pyplot as plt
import os.path as op
import os

pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 1000)
PLOT_FOLDER = 'plots/growth'
DATA_FILE = '../data/pre-processed/cssegi_sand_data/cssegi_agg_data.pickle'
PLOT_NAME = 'loglog_new_confirmed'
GEO_REGION_VAR = 'country'
country = 'Denmark'
N_DAYS_WINDOW = 5

os.makedirs(PLOT_FOLDER, exist_ok=True)

df_all = pd.read_pickle(DATA_FILE)
df_all = df_all.sort_values(by=['date', GEO_REGION_VAR])
df_all['confirmed_new'] = df_all.groupby(GEO_REGION_VAR)['confirmed'].diff()
rolling_var_name = f'confirmed_new_{N_DAYS_WINDOW}_days_rolling_window'
df_all[rolling_var_name] = df_all.groupby(GEO_REGION_VAR)['confirmed_new'].rolling(N_DAYS_WINDOW).sum().reset_index()['confirmed_new']

plot_filename = f'{country}_{PLOT_NAME}.png'.lower()

df = df_all[df_all.country == country]
df.plot(x='confirmed', y=rolling_var_name, title=country, loglog=True)
plt.savefig(op.join(PLOT_FOLDER, plot_filename))
