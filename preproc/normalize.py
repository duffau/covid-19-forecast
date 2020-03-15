from pandas import DataFrame, Series
import re


def normalize_variable_names(df: DataFrame):
    df = df.rename(columns=lambda name: _strip_whitespace(name))
    df = df.rename(columns=lambda name: _replace_whitespace_with_underscore(name))
    df = df.rename(columns=lambda name: _camel_case_to_snake_case(name))
    return df


def _strip_whitespace(name: str):
    return name.strip()


def _replace_whitespace_with_underscore(name: str):
    return re.sub(r'\s+', '_', name)


def _camel_case_to_snake_case(name: str):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()


def normalize_country(series: Series, country_name_mapping: callable):
    return series.map(country_name_mapping, na_action='ignore')

