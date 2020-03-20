import pandas as pd
import os
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 1000)
PLOT_FOLDER = 'plots'
DATA_FILE = '../data/pre-processed/cssegi_sand_data/cssegi_agg_data.pickle'

os.makedirs(PLOT_FOLDER, exist_ok=True)
df = pd.read_pickle(DATA_FILE)
df.info()

for country in df.country.unique():
    print(f"Plotting data for {country} ...")
    try:
        df[df.country == country].plot(x='date', y=['confirmed', 'deaths', 'recovered'], title=country)
        plt.savefig(os.path.join(PLOT_FOLDER, "{}-cumulativ.png".format(country.lower())))
        plt.close()

        df[df.country == country].plot(x='date', y=['total_infected', 'total_removed'])
        plt.savefig(os.path.join(PLOT_FOLDER, "{}-SIR.png".format(country.lower())))
        plt.close()
    except Exception as e:
        print(f"Plotting failed for {country}. Exception: {repr(e)}")
