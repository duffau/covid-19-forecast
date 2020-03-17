from typing import List
import glob
import pandas as pd
import os
import io
from collections import namedtuple

from preproc.known_error import KnownErrors
import preproc.utils as utils
import preproc.clean as clean
import preproc.normalize as normz

CSVFile = namedtuple("CSVFile", ['filename', 'content'])


def run(
        dated_csv_filenames: List[str],
        known_errors: KnownErrors,
        world_pop_csv: str,
        output_folder: str,
):
    csv_files = read_all(dated_csv_filenames)
    csv_files = replace_known_errors(csv_files, known_errors)
    df = csvs_to_dataframe(csv_files)
    df = aggregate_country(df)

    df_world_pop = utils.read_data(world_pop_csv)
    df = add_population(df, df_world_pop)

    df = normz.normalize_variable_names(df)

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
    pickled_path = os.path.join(output_folder, 'nssac_agg_data.pickle')
    df.to_pickle(pickled_path)
    csv_path = os.path.join(output_folder, 'nssac_agg_data.csv')
    df.to_csv(csv_path, index=False)


def read_all(csv_filenames: List[str]) -> List[CSVFile]:
    csvs = []
    for filename in csv_filenames:
        with open(filename) as csv_file:
            csv_content = csv_file.read()
        csvs.append(
            CSVFile(filename, csv_content)
        )
    return csvs


def replace_known_errors(csv_files: List[CSVFile], known_errors: KnownErrors):
    for i, csv_file in enumerate(csv_files):
        base_filename = os.path.basename(csv_file.filename)
        csv_files[i] = csv_file.filename, known_errors.replace(base_filename, csv_file.content)
    return csv_files


def csvs_to_dataframe(csv_files):
    dfs = []
    for filename, csv_content in csv_files:
        df = pd.read_csv(io.StringIO(csv_content), index_col=None, header=0)
        try:
            df = normalize(df)
        except Exception as e:
            raise Exception(f"Normalizing failed for csv: {filename}") from e
        dfs.append(df)
    return pd.concat(dfs, axis=0, ignore_index=True)


def normalize(df):
    df['Last Update'] = clean.clean_datetime(df['Last Update'], timestamp_pattern=r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}")
    df['Last Update'] = utils.parse_date(df['Last Update'], format='%Y-%m-%d %H:%M:%S')
    df = df.rename(columns={'Last Update': 'last_update_ts'})
    df['country'] = normz.normalize_country(df['Region'], nssac_country_map)
    return df


def nssac_country_map(region):
    if 'China' in region:
        return 'China'
    else:
        return region


def aggregate_country(df: pd.DataFrame):
    df = df.drop('name', axis=1)
    df['last_update_date'] = df['last_update_ts'].dt.date
    df = df.drop_duplicates()
    df = df.groupby(['country', 'last_update_date']).sum().reset_index()
    df.sort_values(by=['country', 'last_update_date'])
    df = df.drop_duplicates()
    return df


def add_population(df, df_pop):
    df = pd.merge(df, df_pop[['name', 'pop2019']], how='left', left_on='country', right_on='name')
    df = df.drop('name', axis=1)
    df.pop2019 *= 1000
    df = df.rename(columns={'pop2019': 'population'})
    return df


if __name__ == '__main__':
    from data_prep.nssac_known_errors import nssac_known_errors

    CSV_WORLD_POP = '../data/raw/world_population.csv'
    DATED_CSV_FILES_FOLDER = '../data/raw/nssac/historical'
    PRE_PROCESSED_DATA_FOLDER = '../data/pre-processed/historical'

    dated_csv_file_pattern = os.path.join(DATED_CSV_FILES_FOLDER, 'nssac-ncov-sd-*-2020.csv')
    dated_csv_files = glob.glob(dated_csv_file_pattern)
    print("Found {} csv files matching pattern.".format(len(dated_csv_files)))

    run(dated_csv_filenames=dated_csv_files,
        known_errors=nssac_known_errors,
        world_pop_csv=CSV_WORLD_POP,
        output_folder=PRE_PROCESSED_DATA_FOLDER)
