import os
import urllib
from glob import glob

import dask.bag as db
import numpy as np
import zarr
from dask.diagnostics import ProgressBar
from netCDF4 import Dataset


def download(url):
    opener = urllib.URLopener()
    filename = os.path.basename(url)
    path = os.path.join('data', filename)
    opener.retrieve(url, path)


def download_weather():
    # Create data directory
    if not os.path.exists('data'):
        os.mkdir('data')

    template = ('http://www.esrl.noaa.gov/psd/thredds/fileServer/Datasets/'
                'noaa.oisst.v2.highres/sst.day.mean.{year}.v2.nc')

    urls = [template.format(year=year) for year in range(1981, 2016)]
    b = db.from_sequence(urls, partition_size=1)

    print("Downloading Weather Data")
    print("------------------------")
    with ProgressBar():
        b.map(download).compute(n_workers=8)


def transform_weather():
    if os.path.exists('sst.day.mean.v2.zarr'):
        return
    datasets = [Dataset(path)['sst'] for path in sorted(glob('data/*.nc'))]
    n = sum(d.shape[0] for d in datasets)
    shape = (n, 720, 1440)
    chunks = (72, 360, 360)
    f = zarr.open_array('sst.day.mean.v2.zarr', shape=shape, chunks=chunks,
                        dtype='f4')

    i = 0
    for d in datasets:
        m = d.shape[0]
        f[i:i + m] = d[:].filled(np.nan)
        i += m


if __name__ == '__main__':
    download_weather()
    transform_weather()
