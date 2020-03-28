import pandas as pd
import re


def clean_datetime(series: pd.Series, timestamp_pattern):
    pat = re.compile(r"({ts_pat}).*".format(ts_pat=timestamp_pattern))
    repl = lambda m: m.group(1)
    return series.str.replace(pat, repl)
