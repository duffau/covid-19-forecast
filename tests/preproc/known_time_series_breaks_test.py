import pytest
from preproc.known_time_series_breaks import KnownTimeSeriesBreak
from datetime import datetime
from pandas import DataFrame, Series






@pytest.fixture
def ts_break_scale_and_add_two_dates():
    return KnownTimeSeriesBreak(
        id='Denmark',
        date_intervals=[datetime(2020, 2, 12), datetime(2020, 2, 14)],
        scale_factors=[2, 1, 1],
        additive_offsets=[0, 2, 3],
    )


def test_init():
    KnownTimeSeriesBreak(
        id='Denmark',
        date_intervals=[datetime(2020, 2, 12)],
        additive_offsets=[0, 2]
    )



def test_rescale_add():
    ts_break = KnownTimeSeriesBreak(
        id='something',
        date_intervals=[datetime(2020, 2, 12), datetime(2020, 2, 14)],
        additive_offsets=[0, 2, 3]
    )
    dates = Series([datetime(2020, 2, d) for d in range(11, 16)])
    series = Series([1] * len(dates))
    expected_series = Series([1, 1, 3, 3, 4])
    output_series = ts_break.rescale(series, dates)
    assert (output_series == expected_series).all()


def test_rescale_scale():
    ts_break = KnownTimeSeriesBreak(
        id='something',
        date_intervals=[datetime(2020, 2, 12), datetime(2020, 2, 14)],
        scale_factors=[1, 2, 3]
    )
    dates = Series([datetime(2020, 2, d) for d in range(11, 16)])
    series = Series([1] * len(dates))
    expected_series = Series([1, 1, 2, 2, 3])
    output_series = ts_break.rescale(series, dates)
    assert (output_series == expected_series).all()


def test_rescale_scale_and_add():
    ts_break = KnownTimeSeriesBreak(
        id='something',
        date_intervals=[datetime(2020, 2, 12), datetime(2020, 2, 14)],
        additive_offsets=[0, 3, 5],
        scale_factors=[1, 2, 3]
    )
    dates = Series([datetime(2020, 2, d) for d in range(11, 16)])
    series = Series([2] * len(dates))
    expected_series = Series([2, 2, 7, 7, 11])
    output_series = ts_break.rescale(series, dates)
    assert (output_series == expected_series).all()
