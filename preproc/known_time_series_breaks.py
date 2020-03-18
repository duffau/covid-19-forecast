from typing import List
from datetime import datetime
from pandas import Series


class KnownTimeSeriesBreak:

    def __init__(self, id: str, date_intervals: List[datetime], scale_factors: List[float] = None, additive_offsets: List[float] = None):
        self.id= id
        self.date_intervals = date_intervals

        if scale_factors:
            assert len(scale_factors) == len(date_intervals) + 1, "Scale factors must have same length as date_intervals."
        self.scale_factors = scale_factors

        if additive_offsets:
            assert len(additive_offsets) == len(date_intervals) + 1, "Additive offsets must have same length as date_intervals."
        self.additive_offsets = additive_offsets

    def rescale(self, series: Series, dates: Series):
        rescaled_series = series.copy()

        interval_nr = Series([0]*series.size)
        for dt in self.date_intervals:
            interval_nr += (dates > dt)
        interval_nr = interval_nr.astype('int')

        if self.scale_factors:
            for i, scale in enumerate(self.scale_factors):
                rescaled_series.loc[interval_nr == i] *= scale

        if self.additive_offsets:
            for i, additive_offset in enumerate(self.additive_offsets):
                rescaled_series.loc[interval_nr == i] += additive_offset

        return rescaled_series


class KnownTimeSeriesBreaks:

    def __init__(self):
        self.known_ts_breaks = {}

    def add(self, known_ts_break: KnownTimeSeriesBreak):
        self.known_ts_breaks[known_ts_break.id] = known_ts_break

    def rescale(self, df, id_column):
        df_rescaled = df.copy()
        return df_rescaled
