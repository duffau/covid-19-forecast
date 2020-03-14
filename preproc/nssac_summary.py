import pandas as pd
import os
import re


def read_data(filepath):
    df = pd.read_csv(filepath)
    return df


def parse_date_col(df, format):
    df.date = pd.to_datetime(df.date, format=format)
    return df


def add_constant_variables(df, names, values):
    for name, value in zip(names, values):
        df[name] = value
    return df


def rename_variables(df):
    return df.rename(columns=lambda name: re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower())


def construct_variables(df):
    df['total_removed'] = df.total_recovered + df.total_deaths
    df['total_infected'] = df.total_confirmed - df.total_removed
    df['total_susceptible'] = df.total_population - df.total_removed - df.total_infected
    return df


def preprocess(df):
    DATE_FORMAT = "%m-%d-%Y"
    df = parse_date_col(df, DATE_FORMAT)
    df = construct_variables(df)
    return df


def save(df, org_filepath, folder):
    base_filename, _ = os.path.splitext(os.path.basename(org_filepath))
    filename = base_filename + '.pickle'
    filepath = os.path.join(folder, filename)
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    df.to_pickle(filepath)


def get_population_size(df_world_pop, country):
    return df_world_pop[df_world_pop.name == country]['pop2019'].iloc[0] * 1000


def run(csv_file, world_pop_csv, output_folder):
    df = read_data(csv_file)
    df_world_pop = read_data(world_pop_csv)
    df = add_constant_variables(
        df,
        names=['total_population'],
        values=[get_population_size(df_world_pop, "World")]
    )
    df = rename_variables(df)
    df = preprocess(df)
    save(df, csv_file, output_folder)


if __name__ == '__main__':
    CSV_WORLD_POP = '../data/raw/world_population.csv'
    CSV_FILE = '../data/raw/historical/nssac-ncov-sd-summary.csv'
    PRE_PROCESSED_DATA_FOLDER = '../data/pre-processed/historical'
    run(CSV_FILE, CSV_WORLD_POP, PRE_PROCESSED_DATA_FOLDER)
