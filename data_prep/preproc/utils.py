import pandas as pd
import os


def read_data(filepath):
    if filepath.endswith('.csv'):
        df = pd.read_csv(filepath)
    elif filepath.endswith('.pickle'):
        df = pd.read_pickle(filepath)
    else:
        raise ValueError(f'Invalid file format of {filepath}')
    return df


def parse_date(series, format):
    return pd.to_datetime(series, format=format)


def add_constant_variables(df, names, values):
    for name, value in zip(names, values):
        df[name] = value
    return df


def construct_sir_variables(df, recovered_name='total_recovered',
                            deaths_name='total_deaths',
                            cases_name='total_confirmed',
                            population_name='total_population'):
    df['total_removed'] = df[recovered_name] + df[deaths_name]
    df['total_infected'] = df[cases_name] - df.total_removed
    df['total_susceptible'] = df[population_name] - df.total_removed - df.total_infected
    return df


def preprocess(df):
    DATE_FORMAT = "%m-%d-%Y"
    df.date = parse_date(df.date, DATE_FORMAT)
    df = construct_sir_variables(df)
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