import pandas as pd
from forecast import forecast_countries, StartParams, ForecastInfo, extract_cssegi_forecast_info

DATA_FILE = '../data/pre-processed/cssegi_sand_data/cssegi_agg_data.pickle'
df_all = pd.read_pickle(DATA_FILE)

start_params = {
    'Denmark': StartParams(beta=0.35, gamma=0.04, I0=1),
    'China': StartParams(beta=0.35, gamma=0.04, I0=200)
}

