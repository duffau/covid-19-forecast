import pandas as pd
import os
import matplotlib.pyplot as plt

PLOT_FOLDER = 'plots'
DATA_FILE = '../data/pre-processed/historical/nssac-ncov-sd-summary.pickle'
df = pd.read_pickle(DATA_FILE)
print(df.info())

df.plot(x='date', y=['total_confirmed', 'total_deaths', 'total_recovered'])
plt.savefig(os.path.join(PLOT_FOLDER, "nssac-ncov-sd-summary_cumulativ.png"))
plt.close()

df.plot(x='date', y=['total_infected', 'total_removed'])
plt.savefig(os.path.join(PLOT_FOLDER, "nssac-ncov-sd-summary_cumulativ_SIR.png"))
plt.close()
