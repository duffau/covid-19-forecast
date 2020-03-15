import re


def normalize_variable_names(df):
    df = df.rename(columns=lambda name: _replace_whitespace_with_underscore(name))
    df = df.rename(columns=lambda name: _camel_case_to_snake_case(name))
    return df


def _replace_whitespace_with_underscore(name):
    return re.sub(r'\s', '_', name)


def _camel_case_to_snake_case(name):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()