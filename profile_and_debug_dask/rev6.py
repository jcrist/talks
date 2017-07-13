import dask.dataframe as dd
import pandas as pd


df = dd.read_parquet('flights.parquet')


def counts_by_origin(df):
    meta = dd.utils.make_meta([('EWR', 'i8'), ('JFK', 'i8'), ('LGA', 'i8')],
                              index=pd.DatetimeIndex([], name='Date'))

    by_month = df.map_partitions(lambda df: df.resample('MS').Origin.value_counts().unstack(),
                                 meta=meta)
    by_year = by_month.resample('AS').sum()

    return by_month, by_year
