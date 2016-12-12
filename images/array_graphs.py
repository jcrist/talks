import dask
import dask.array as da

kwargs = {'bgcolor': '#00000000',
          'rankdir': 'BT',
          'node_attr': {'color': 'black',
                        'fontcolor': '#000000',
                        'penwidth': '3'},
          'edge_attr': {'color': 'black', 'penwidth': '3'}}

x = da.ones((15, 15), chunks=(5, 5))

x.mean(split_every=10).visualize('array-mean.svg', **kwargs)
(x + x.T).visualize('array-xxT.svg', **kwargs)
(x.dot(x.T + 1)).visualize('array-xdotxT.svg', **kwargs)
(x.dot(x.T + 1) - x.mean()).visualize('array-xdotxT-mean.svg', **kwargs)
(x.dot(x.T + 1) - x.mean()).std().visualize('array-xdotxT-mean-std.svg', **kwargs)


N = 25
x = da.ones((N, N), chunks=(5, 5))
xxT = x + x.T
U, S, V = da.linalg.svd(xxT.rechunk((5, N)) - x.mean())
dask.visualize(U, S, V, filename='array-svd.svg', **kwargs)
