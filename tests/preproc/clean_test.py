import pytest
import data_prep.preproc.clean as clean
from pandas import Series

@pytest.fixture
def timestamp_pattern():
    return r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"

@pytest.fixture
def clean_dates():
    date_strings = [
        "2020-02-03 03:53:00",
        "2020-01-29 21:00:00",
        "2020-01-29 02:90:00"
    ]
    return Series(data=date_strings)


@pytest.fixture
def dirty_dates():
    date_strings = [
        "2020-02-03 03:53:00 * CTY: LA 1; Orange 1; 2 Santa Clara; 2 San Benito",
        "2020-01-29 21:00:00 * CTY: LA 1; Orange ",
        "2020-01-29 02:90:00"
    ]
    return Series(data=date_strings)


def test_clean_date(dirty_dates, clean_dates, timestamp_pattern):
    output_clean_dates = clean.clean_datetime(dirty_dates, timestamp_pattern)
    assert (output_clean_dates == clean_dates).all()
