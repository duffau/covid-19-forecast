from fuzzywuzzy import process
import pandas as pd
from pandas.core.common import SettingWithCopyWarning
import warnings


def fuzzy_left_merge(left, right, left_on=None, right_on=None, threshold=90, **kwargs):
    """
    From Erfan's answer: https://stackoverflow.com/questions/13636848/is-it-possible-to-do-fuzzy-match-merge-with-python-pandas
    df_1 is the left table to join
    df_2 is the right table to join
    key1 is the key column of the left table
    key2 is the key column of the right table
    threshold is how close the matches should be to return a match, based on Levenshtein distance
    limit is the amount of matches that will get returned, these are sorted high to low
    """

    warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)

    left_on_org = left[left_on].copy()
    # First merging on exact matches
    df = pd.merge(left, right, how='left', left_on=left_on, right_on=right_on, **kwargs)
    unmatched_bool_filter = df.isnull().any(axis=1)
    matched_keys = set(df[df.notnull().all(axis=1)][left_on])

    right_keys = set(right[right_on].tolist())
    right_keys_to_match = right_keys.difference(matched_keys)
    left[left_on][unmatched_bool_filter] = left[unmatched_bool_filter][left_on].apply(lambda x: process.extract(x, right_keys_to_match, limit=1)[0])
    left[left_on][unmatched_bool_filter] = left[unmatched_bool_filter][left_on].apply(lambda x: x[0] if x[1] >= threshold else None)

    df = pd.merge(left, right, how='left', left_on=left_on, right_on=right_on, **kwargs)
    df[left_on] = left_on_org
    return df
