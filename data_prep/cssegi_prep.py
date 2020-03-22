from typing import List, Union
import pandas as pd
import re
import os
import os.path as op
from functools import reduce

from preproc.known_error import KnownErrors
import preproc.utils as utils
import preproc.normalize as normz

COL_DATE_RE_PATTERN = r'\d{1,2}/\d{1,2}/\d{1,2}'
COL_DATE_DATE_FORMAT = '%m/%d/%y'
LEFT_FILENAME_BASE = 'time_series_19-covid-'
pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 1000)


def run(csv_file_paths: List[str],
        known_errors: Union[KnownErrors, None],
        world_pop_csv: str,
        output_folder: str, ):
    dfs = []
    for csv_file_path in csv_file_paths:
        var_name = extract_var_name(csv_file_path)
        df = pd.read_csv(csv_file_path)
        df = append_x_to_date_columns(df)
        df = pd.wide_to_long(df, stubnames=['x'], i=['Province/State', 'Country/Region'], j='date', suffix=COL_DATE_RE_PATTERN)
        df.reset_index(inplace=True)
        df.rename(columns={'x': var_name}, inplace=True)
        df.date = pd.to_datetime(df.date, format=COL_DATE_DATE_FORMAT)
        df = df.drop(labels=['Province/State', 'Long', 'Lat'], axis=1)
        df = df.groupby(['Country/Region', 'date']).sum().reset_index()
        df = df.sort_values(by=['Country/Region', 'date'])
        dfs.append(df)
    df = reduce(lambda x, y: pd.merge(x, y, on=['Country/Region', 'date']), dfs)
    df = normz.normalize_variable_names(df, mapping={'Country/Region': 'country', 'Death': 'deaths'})
    df_world_pop = utils.read_data(world_pop_csv)
    df = add_population(df, df_world_pop)

    df = utils.construct_sir_variables(
        df,
        recovered_name='recovered',
        deaths_name='deaths',
        cases_name='confirmed',
        population_name='population'
    )

    print("\nAggregated df:")
    df.info()
    print("\nIs NA:")
    print(utils.column_na_stats(df))

    pickled_path = op.join(output_folder, 'cssegi_agg_data.pickle')
    df.to_pickle(pickled_path)
    csv_path = op.join(output_folder, 'cssegi_agg_data.csv')
    df.to_csv(csv_path, index=False)


def extract_var_name(csv_file_path):
    return op.basename(csv_file_path).lstrip(LEFT_FILENAME_BASE).rstrip('.csv')


def append_x_to_date_columns(df: pd.DataFrame):
    return df.rename(columns=lambda s: 'x' + str(s) if is_date(str(s)) else s)


def is_date(s):
    pat = re.compile('^' + COL_DATE_RE_PATTERN + '$')
    return re.match(pat, s)


def add_population(df, df_pop):
    df = pd.merge(df, df_pop[['name', 'pop2019']], how='left', left_on='country', right_on='name')
    df = df.drop('name', axis=1)
    df.pop2019 *= 1000
    df = df.rename(columns={'pop2019': 'population'})
    return df


def main():
    CSV_WORLD_POP = '../data/raw/world_population.csv'
    CONFIRMED_CSV_FILE_PATH = '../data/raw/cssegi_sand_data/time_series_19-covid-Confirmed.csv'
    DEATHS_CSV_FILE_PATH = '../data/raw/cssegi_sand_data/time_series_19-covid-Deaths.csv'
    RECOVERED_CSV_FILE_PATH = '../data/raw/cssegi_sand_data/time_series_19-covid-Recovered.csv'
    PRE_PROCESSED_DATA_FOLDER = '../data/pre-processed/cssegi_sand_data'
    os.makedirs(PRE_PROCESSED_DATA_FOLDER, exist_ok=True)
    run(
        csv_file_paths=[CONFIRMED_CSV_FILE_PATH, DEATHS_CSV_FILE_PATH, RECOVERED_CSV_FILE_PATH],
        known_errors=None,
        world_pop_csv=CSV_WORLD_POP,
        output_folder=PRE_PROCESSED_DATA_FOLDER
    )


if __name__ == '__main__':
    main()
