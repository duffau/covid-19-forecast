from typing import List, Union
import pandas as pd
import re
import os.path as op
from functools import reduce
import logging

from data_prep.preproc.known_error import KnownErrors
import data_prep.preproc.utils as utils
import data_prep.preproc.normalize as normz
import data_prep.fuzzy_merge as fuz

COL_DATE_RE_PATTERN = r'\d{1,2}/\d{1,2}/\d{1,2}'
COL_DATE_DATE_FORMAT = '%m/%d/%y'
VAR_NAME_PATTERN = '^time_series_covid19_(\w+)_global.csv$'

COUNTRY_RENAME = {
    'US': 'United States'
}

pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 1000)
logger = logging.getLogger(__name__)


def run(csv_file_paths: List[str],
        known_errors: Union[KnownErrors, None],
        world_pop_file: str,
        world_hosp_beds_file: str,
        output_file: str, ):
    dfs = []
    for csv_file_path in csv_file_paths:
        print(f'Loading {csv_file_path} and appending ...')
        var_name = extract_var_name(csv_file_path)
        df = pd.read_csv(csv_file_path)
        df = append_x_to_date_columns(df)
        df.info()
        df = pd.wide_to_long(df, stubnames=['x'], i=['Province/State', 'Country/Region'], j='date', suffix=COL_DATE_RE_PATTERN)
        df.reset_index(inplace=True)
        df.rename(columns={'x': var_name}, inplace=True)
        df.date = pd.to_datetime(df.date, format=COL_DATE_DATE_FORMAT)
        df['Country/Region'] = df['Country/Region'].replace(to_replace=COUNTRY_RENAME)
        df = df.drop(labels=['Province/State', 'Long', 'Lat'], axis=1)
        df = df.groupby(['Country/Region', 'date']).sum().reset_index()
        df = df.sort_values(by=['Country/Region', 'date'])
        dfs.append(df)
    df = reduce(lambda x, y: pd.merge(x, y, on=['Country/Region', 'date']), dfs)
    df = normz.normalize_variable_names(df, mapping={'Country/Region': 'country', 'Death': 'deaths'})

    df_world_pop = utils.read_data(world_pop_file)
    df = add_population(df, df_world_pop)

    df_world_hosp_beds = utils.read_data(world_hosp_beds_file)
    df = add_hosp_beds(df, df_world_hosp_beds)

    df = utils.construct_sir_variables(
        df,
        recovered_name='recovered',
        deaths_name='deaths',
        cases_name='confirmed',
        population_name='population'
    )

    print("\nIs NA:")
    print(utils.column_na_stats(df))

    df.to_pickle(output_file)


def extract_var_name(csv_file_path):
    return re.match(VAR_NAME_PATTERN, op.basename(csv_file_path)).group(1)


def append_x_to_date_columns(df: pd.DataFrame):
    return df.rename(columns=lambda s: 'x' + str(s) if is_date(str(s)) else s)


def is_date(s):
    pat = re.compile('^' + COL_DATE_RE_PATTERN + '$')
    return re.match(pat, s)


def add_population(df, df_pop):
    print('Adding population variable ...')
    df = fuz.fuzzy_left_merge(df, df_pop[['Country Name', 'Fact']], left_on='country', right_on='Country Name')
    df = df.drop('Country Name', axis=1)
    df = df.rename(columns={'Fact': 'population'})
    for country, pop in POPULATIONS.items():
        df['population'][df.country == country] = pop
    nan_countries = df.country[pd.isna(df.population)].unique()
    nan_countries = "\n".join(nan_countries)
    logger.info(f'\nCountries with NAN population:\n{nan_countries}')
    return df


def add_hosp_beds(df, df_beds):
    print('Adding hospital beds variable ...')
    df = fuz.fuzzy_left_merge(df, df_beds[['Country Name', 'Fact']], left_on='country', right_on='Country Name')
    df = df.drop('Country Name', axis=1)
    df = df.rename(columns={'Fact': 'hospital_beds_per_thousand_cap'})
    df['hospital_beds_total'] = df.population * df.hospital_beds_per_thousand_cap / 1000
    nan_countries = df.country[pd.isna(df.hospital_beds_total)].unique()
    nan_countries = "\n".join(nan_countries)
    logger.info(f'\nCountries with NAN hospital_beds_total:\n{nan_countries}')
    return df


POPULATIONS = {
    'Taiwan*': 23773876,
    'Korea, South': 51606633,
    'Slovakia': 5446771,
    'Burma': 53708395,
}