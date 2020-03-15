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
    df = pd.merge(df, df_world_pop[['name', 'pop2019']], how='left', left_on='Region', right_on='name')
    del df['name']
    df = normz.normalize_variable_names(df)
    print("\nAggregated df:")
    df.info()
    print("\nIs NA:")
    print(utils.column_na_stats(df))
    pickled_path = os.path.join(output_folder, 'nssac_agg_data.pickle')
    df.to_pickle(pickled_path)


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
    return df


def aggregate_country(df):
    df = df.drop('name', axis=1)
    return df.groupby(['Region', 'Last Update']).sum().reset_index()


if __name__ == '__main__':
    from preproc.nssac_known_errors import nssac_known_errors

    CSV_WORLD_POP = '../data/raw/world_population.csv'
    DATED_CSV_FILES_FOLDER = '../data/raw/historical'
    PRE_PROCESSED_DATA_FOLDER = '../data/pre-processed/historical'

    dated_csv_file_pattern = os.path.join(DATED_CSV_FILES_FOLDER, 'nssac-ncov-sd-*-2020.csv')
    dated_csv_files = glob.glob(dated_csv_file_pattern)
    print("Found {} csv files matching pattern.".format(len(dated_csv_files)))

    run(dated_csv_filenames=dated_csv_files,
        known_errors=nssac_known_errors,
        world_pop_csv=CSV_WORLD_POP,
        output_folder=PRE_PROCESSED_DATA_FOLDER)
