## Minneanalytics "Big Data Tech 2017"

Materials for my talk on Dask & Numba at [Big Data Tech
2017](http://minneanalytics.org/bigdatatech-2017/) put on by
[Minneanalytics](http://minneanalytics.org/).

Slides can be viewed [here](http://jcrist.github.io/talks/minneanlytics_2017/slides.html).

The rendered example notebook can be viewed
[here](http://nbviewer.jupyter.org/github/jcrist/talks/blob/master/minneanalytics_2017/Ocean%20Temperature%20Data.ipynb).

### Setup environment

```bash
$ conda create -n dask_demo python=3.5
$ source activate dask_demo
$ conda install dask distributed jupyter matplotlib numba zarr -c conda-forge
```

### Downloading example data

The ocean temperature example uses a full dataset from the
[esrl.noaa.gov](http://www.esrl.noaa.gov/psd/thredds/dodsC/Datasets/noaa.oisst.v2.highres/catalog.html)
catalog. To download the data, run the `get_data.py` script. Note that
depending on your connection, this may take a very long time. It will download
~15 GB of data to disk, then convert it to a `zarr` array.
