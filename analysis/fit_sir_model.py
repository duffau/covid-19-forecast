import pandas as pd
import os
import matplotlib.pyplot as plt

PLOT_FOLDER = 'plots'
CSV_FILE = '../data/historical/nssac-ncov-sd-summary.csv'
DATE_FORMAT = "%m-%d-%Y"
df = pd.read_csv(CSV_FILE)
df.date = pd.to_datetime(df.date, format=DATE_FORMAT)
print(df.info())

df.plot(x='date', y=['totalConfirmed', 'totalDeaths', 'totalRecovered'])
plt.savefig(os.path.join(PLOT_FOLDER, "nssac-ncov-sd-summary_cumulativ.png"))

df.plot(x='date', y=['newConfirmed', 'newDeaths', 'newRecovered'])
plt.savefig(os.path.join(PLOT_FOLDER,"nssac-ncov-sd-summary_delta.png"))
