import os
from .start_params import *

THIS_DIR = os.path.dirname(os.path.realpath(__file__))
DATA_DIR = os.path.join(THIS_DIR, '../data')

_CSSEGI_SAND_DATA = 'cssegi_sand_data'
_WORLD_BANK = 'world_bank'

RAW_DATA_DIR = os.path.join(DATA_DIR, 'raw')
CSSEGI_RAW_DATA_DIR = os.path.join(RAW_DATA_DIR, _CSSEGI_SAND_DATA)
WORLD_BANK_RAW_DATA_DIR = os.path.join(RAW_DATA_DIR, _WORLD_BANK)

PREPROC_DATA_DIR = os.path.join(DATA_DIR, 'pre-processed')
CSSEGI_PREPROC_DATA_DIR = os.path.join(PREPROC_DATA_DIR, _CSSEGI_SAND_DATA)
CSSEGI_PREPROC_DATA_FILE = os.path.join(CSSEGI_PREPROC_DATA_DIR, 'cssegi_agg_data.pickle')
WORLD_BANK_PREPROC_DATA_DIR = os.path.join(PREPROC_DATA_DIR, _WORLD_BANK)

CONFIRMED_FILENAME_CSV = 'time_series_covid19_confirmed_global.csv'
DEATHS_FILENAME_CSV = "time_series_covid19_deaths_global.csv"
RECOVERED_FILENAME_CSV = "time_series_covid19_recovered_global.csv"
HOSP_BEDS_FILENAME_CSV = 'hospital_beds.csv'
HOSP_BEDS_FILENAME_PICKLE = 'hospital_beds.pickle'
POP_FILENAME_CSV = 'population.csv'
POP_FILENAME_PICKLE = 'population.pickle'

FORECAST_TS_DIR = os.path.join(DATA_DIR, 'forecasts', 'time_series')
FORECAST_INFO_DIR = os.path.join(DATA_DIR, 'forecasts', 'info')

FORECAST_PLOT_FOLDER = os.path.join(THIS_DIR, '../forecast_plots')
README_FILE = os.path.join(THIS_DIR, '../README.md')

# Forecast config
N_DAYS_PREDICT = 400
COUNTRIES = ['Denmark', 'Iran', 'Spain', 'Italy', 'Sweden']
SKIP_COUNTRIES = []
SEED = 43
START_PARAMS = SIR_CF_START_PARAMS
