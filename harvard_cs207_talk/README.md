## Harvard CS207 Guest Lecture Materials

These are the slides and notebooks for a guest lecture about Dask given to
[Harvard CS207](https://iacs-cs207.github.io/cs207-2016/) on 11/30/16.

Slides can be viewed [here](http://jcrist.github.io/talks/harvard_cs207_talk/slides.html).

The `dask_array` and `dask_dataframe` notebooks should be runnable locally,
while the `dask_dataframe_cluster` notebook relies on some local data that
isn't public.

### Setup

- Clone the repo
- Install `conda`

```bash
$ conda create -n harvard_dask python=3.5
$ source activate harvard_dask
$ conda install dask distributed bokeh jupyter -c conda-forge
```

### More Resources

For a more information, please check out the following resources:

- [Dask Documentation](http://dask.pydata.org/)
- [Dask Tutorial](https://github.com/dask/dask-tutorial)
- [Dask Repository](https://github.com/dask/dask)
- [Dask Gitter Chatroom](https://gitter.im/dask/dask)

If you have any questions or wish to contribute (we love new contributors),
please feel free to reach out via github issues or via gitter.
