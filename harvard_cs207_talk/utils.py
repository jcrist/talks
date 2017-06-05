import os
import numpy as np


if not os.path.exists('data'):
    os.mkdir('data')


def random_array():
    if os.path.exists(os.path.join('data', 'random.hdf5')):
        return

    import h5py
    print("Creating random data for array notebook")
    N = 12500
    chunk = 2500

    with h5py.File(os.path.join('data', 'random.hdf5')) as f:
        dset = f.create_dataset('/x', shape=(N, N), dtype='f8')
        for i in range(0, N, chunk):
            for j in range(0, N, chunk):
                dset[i: i + chunk, j: j + chunk] = np.random.normal(size=(chunk, chunk))


def accounts_csvs(num_files, n, k):
    fn = os.path.join('data', 'accounts.%d.csv' % (num_files - 1))

    if os.path.exists(fn):
        return

    print("Create random data for dataframe notebook")

    args = account_params(k)

    for i in range(num_files):
        df = account_entries(n, *args)
        df.to_csv(os.path.join('data', 'accounts.%d.csv' % i),
                  index=False)


names = ['Alice', 'Bob', 'Charlie', 'Dan', 'Edith', 'Frank', 'George',
         'Hannah', 'Ingrid', 'Jerry', 'Kevin', 'Laura', 'Michael', 'Norbert',
         'Oliver', 'Patricia', 'Quinn', 'Ray', 'Sarah', 'Tim', 'Ursula',
         'Victor', 'Wendy', 'Xavier', 'Yvonne', 'Zelda']


def account_params(k):
    ids = np.arange(k, dtype=int)
    names2 = np.random.choice(names, size=k, replace=True)
    wealth_mag = np.random.exponential(100, size=k)
    wealth_trend = np.random.normal(10, 10, size=k)
    freq = np.random.exponential(size=k)
    freq /= freq.sum()

    return ids, names2, wealth_mag, wealth_trend, freq


def account_entries(n, ids, names, wealth_mag, wealth_trend, freq):
    import pandas as pd
    indices = np.random.choice(ids, size=n, replace=True, p=freq)
    amounts = ((np.random.normal(size=n) +
                wealth_trend[indices]) * wealth_mag[indices])

    return pd.DataFrame({'id': indices,
                         'names': names[indices],
                         'amount': amounts.astype('i4')},
                         columns=['id', 'names', 'amount'])
