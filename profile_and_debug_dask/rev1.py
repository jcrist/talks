import glob
import pandas as pd



def counts_by_origin():
    frames = []
    # For each file
    for f in sorted(glob.glob('data/*.csv')):
        # Load the dataframe
        df = pd.read_csv(f,
                         parse_dates={'Date': [0, 1, 2]},
                         infer_datetime_format=True)

        # Store in list of frames
        frames.append(df)

    # concatenate all the frames together
    df = pd.concat(frames)

    # Resample by month
    by_month = (df.resample('MS', on='Date')
                  .Origin.value_counts()
                  .unstack())

    # Resample by year
    by_year = (df.resample('AS', on='Date')
                 .Origin.value_counts()
                 .unstack())

    return by_month, by_year
