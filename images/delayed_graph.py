from dask import delayed

kwargs = {'bgcolor': '#00000000',
          'rankdir': 'BT',
          'node_attr': {'color': 'black',
                        'fontcolor': '#000000',
                        'penwidth': '3'},
          'edge_attr': {'color': 'black', 'penwidth': '3'}}


@delayed(pure=True)
def fit1(a):
    pass


@delayed(pure=True)
def fit2(y, b):
    pass


@delayed(pure=True)
def fit3(y, c):
    pass


@delayed(pure=True)
def score(results):
    pass


A = range(3)
B = range(4)
C = range(2)

results = {}

for a in A:
    for b in B:
        for c in C:
            results[a, b, c] = fit3(fit2(fit1(a), b), c)
            best = score(results)

best.visualize('delayed-graph.svg', **kwargs)
