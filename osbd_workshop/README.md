## OSBD Workshop Materials

Materials for my talk on Dask & Numba at the Open Science in Big Data workshop
[(OSBD 2016)](https://osbd.github.io/).

The rendered example notebook can be viewed
[here](http://nbviewer.jupyter.org/github/jcrist/talks/blob/master/osbd_workshop/Ocean%20Temperature%20Data.ipynb).

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
