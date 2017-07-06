import dask.dataframe as dd


def load_data():
    df = dd.read_csv('s3://dask-data/airline-data/199[1,2,3,4,5]*.csv',
                     usecols=['Year', 'Month', 'DayofMonth', 'Origin', 'DepDelay'],
                     dtype={'Origin': 'category'},
                     parse_dates={'Date': [0, 1, 2]},
                     infer_datetime_format=True,
                     storage_options=dict(anon=True))
    return df
