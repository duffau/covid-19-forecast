import pandas as pd
import os


def read_data(filepath):
    df = pd.read_csv(filepath)
    return df


def parse_date(series, format):
    return pd.to_datetime(series, format=format)


def add_constant_variables(df, names, values):
    for name, value in zip(names, values):
        df[name] = value
    return df


def construct_variables(df):
    df['total_removed'] = df.total_recovered + df.total_deaths
    df['total_infected'] = df.total_confirmed - df.total_removed
    df['total_susceptible'] = df.total_population - df.total_removed - df.total_infected
    return df


def preprocess(df):
    DATE_FORMAT = "%m-%d-%Y"
    df.date = parse_date(df.date, DATE_FORMAT)
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


def column_na_stats(df):
    return df.isna().sum(axis=0)