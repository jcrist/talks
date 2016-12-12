## OSBD Workshop Materials

Materials for my talk on Dask & Numba at OSBD 2016.

### Setup environment

```bash
$ conda create -n osbd python=3.5
$ source activate osbd
$ conda install dask distributed jupyter matplotlib numba zarr -c conda-forge
```

### Downloading example data

The ocean temperature example uses a full dataset from the
[esrl.noaa.gov](http://www.esrl.noaa.gov/psd/thredds/dodsC/Datasets/noaa.oisst.v2.highres/catalog.html)
catalog. To download the data, run the `get_data.py` script. Note that
depending on your connection, this may take a very long time. It will download
~15 GB of data to disk, then convert it to a `zarr` array.
