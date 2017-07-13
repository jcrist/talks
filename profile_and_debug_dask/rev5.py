import glob
import pandas as pd
from dask import delayed


@delayed
def load_file(f):
    return pd.read_csv(f,
                       usecols=['Year', 'Month', 'DayofMonth', 'Origin'],
                       dtype={'Origin': 'category'},
                       parse_dates={'Date': [0, 1, 2]},
                       infer_datetime_format=True)


@delayed
def count_flights(df):
    return (df.resample('MS', on='Date')
              .Origin.value_counts()
              .unstack())


@delayed
def merge_counts(counts):
    return pd.concat(counts)


@delayed
def count_by_year(df):
    return df.resample('AS').sum()


def counts_by_origin():
    results = []
    # For each file
    for f in sorted(glob.glob('data/*.csv')):
        df = load_file(f)
        r = count_flights(df)
        results.append(r)

    by_month = merge_counts(results)

    by_year = count_by_year(by_month)

    return by_month, by_year
