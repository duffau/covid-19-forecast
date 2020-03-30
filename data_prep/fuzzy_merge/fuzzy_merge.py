from fuzzywuzzy import process
import pandas as pd


def fuzzy_left_merge(df_1, df_2, key1, key2, threshold=90, **kwargs):
    """
    From Erfan's answer: https://stackoverflow.com/questions/13636848/is-it-possible-to-do-fuzzy-match-merge-with-python-pandas
    df_1 is the left table to join
    df_2 is the right table to join
    key1 is the key column of the left table
    key2 is the key column of the right table
    threshold is how close the matches should be to return a match, based on Levenshtein distance
    limit is the amount of matches that will get returned, these are sorted high to low
    """
    s = df_2[key2].tolist()

    df_1[key1] = df_1[key1].apply(lambda x: process.extract(x, s, limit=1)[0])
    df_1[key1] = df_1[key1].apply(lambda x: x[0] if x[1] >= threshold else None)

    df = pd.merge(df_1, df_2, how='left', left_on=key1, right_on=key2, **kwargs)
    return df
