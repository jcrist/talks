## Dask: Flexible Parallelism

<img src="../images/dask_icon.svg" width=20%>

Jim Crist

Continuum Analytics

<hr width=40%>

*Harvard CS207, 11/30/16*

~~~

Materials can be found on github [here](https://github.com/jcrist/talks/tree/master/harvard_cs207_talk)

~===~

### In the beginning...

- Scientific Python goes back to 1995, with Numeric

<img src="../images/computer_article_1995.jpeg" width=80%>

~~~

### Moore's Law

The number of transistors in a chip ~doubles every two years.

~~~

### Moore's Law

<img src="../images/moores_law.png" width=80%>

~~~

### Hard drives are getting cheaper

<img src="../images/harddrive-cost.png">

~~~

### As are large workstations

[Amazon EC2 Pricing](http://www.ec2instances.info/)

~===~

### Python has a fast and pragmatic data science ecosystem

---

### ... restricted to a single core :(

~~~

### Most Python programs

<img src="../images/cpu_usage.gif" width=200%>

~~~

### The SciPy ecosystem

*  **NumPy**: arrays
*  **Pandas**: tables
*  **Scikit Learn**: machine learning
*  **Statsmodels**: statistics
*  ...
*  ...
*  **GeoPandas**: geo-spatial
*  **Scikit-Image**: image analysis
*  **Scikit-Bio**: ...

~~~

### How do we exploit these improvements

---

### ... without rewriting everything?

~===~

<img src="../images/dask_horizontal_white.svg"
     alt="Dask logo"
     width="50%">

### a flexible library for parallelism

~===~

## Dask is:

- A parallel computing framework

- Written in pure Python

- That leverages the excellent Python ecosystem

- Using blocked algorithms and task scheduling

~~~

### Blocked Algorithms

**Blocked Mean**

```python
x = h5py.File('data.hdf5')['x']    # Trillion element array on disk

sums = []
counts = []
N = 1000000
for i in range(N):                  # One million times
    chunk = x[N*i: N*(i+1)]         # Pull out chunk
    sums.append(np.sum(chunk))      # Sum chunk
    counts.append(len(chunk))       # Count chunk

result = sum(sums) / sum(counts)    # Aggregate results
```

~~~

### Blocked Algorithms

<img src="../images/array-mean-white.svg" width="100%">

~~~

### Task Graphs

- Represent inter-dependent computations as a *graph*
    * Specifically a *Directed Acyclic Graph* (DAG)

~~~

### Task Graphs

<img src="../images/graph.svg" height="20%" align="left" style="margin: 15px 60px">

~~~

### Task Graphs

<img src="../images/graph.svg" height="20%" align="left" style="margin: 15px 60px">
<img src="../images/directed-graph.svg" height="20%" align="left" style="margin: 15px 60px">

~~~

### Task Graphs

<img src="../images/graph.svg" height="20%" align="left" style="margin: 15px 60px">
<img src="../images/directed-graph.svg" height="20%" align="left" style="margin: 15px 60px">
<img src="../images/directed-acyclic-graph.svg" height="20%" align="left" style="margin: 15px 20px">

~~~

### Task Graphs

- Nodes are *tasks* in the graph
    * Rectangles represent data
    * Circles represent computation

- Edges are data dependencies

<img src="../images/array-mean-white.svg" width="90%">

~~~

### Task Graphs

- DAGs have a *topological ordering*
    * Can be arranged such that for every edge `a->b`,  `a` comes before `b` in the ordering.

<img src="../images/directed-acyclic-graph.svg" height="20%" align="left">

- Not necessarily unique
    * ``a, b, c, d`` 
    * ``a, b, d, c``


~~~

### Task Scheduling

- Scheduler takes in graphs and runs the specified tasks, often in parallel

- Task schedulers are common (Make, MapReduce, Spark, Airflow, etc...)

<img src="../images/grid_search_schedule-0.png" width="80%">

~~~

### Task Scheduling

- Scheduler takes in graphs and runs the specified tasks, often in parallel

- Task schedulers are common (Make, MapReduce, Spark, Airflow, etc...)

<img src="../images/grid_search_schedule.gif" width="80%">

~===~

### Dask Stack

<img src="../images/dask-stack-0.svg" width="70%">

~~~

### Dask Stack

<img src="../images/dask-stack-2.svg" width="70%">

~~~

### Dask Stack

<img src="../images/dask-stack-3.svg" width="70%">

~~~

### Dask Stack

<img src="../images/dask-stack-4.svg" width="70%">

~~~

### Dask Stack

<img src="../images/dask-stack-5.svg" width="70%">

~===~

### Dask Array

- Parallel and out-of-core array library
- Mirrors NumPy interface
- Coordinate many NumPy arrays into single logical Dask array

<img src="../images/dask-array-white.svg"
     alt="Dask array is built from many numpy arrays"
     width="70%">

~~~

### Example

~===~

### Dask Dataframe

- Parallel and out-of-core dataframe library
- Mirrors the Pandas interface
- Coordinates many Pandas DataFrames into single logical Dask DataFrame
- Index is (optionally) sorted, allowing for optimizations

<img src="../images/dask-dataframe-white.svg" align="center" width=30%>

~~~

### Example

~===~

### Dask Bag

- Parallel collection of python objects
- Builds off `toolz`/`cytoolz`

```python
>>> import dask.bag as db
>>> import json

>>> records = db.read_text('path/to/data.*.json.gz').map(json.loads)

>>> records.filter(...).pluck('name').frequencies().topk(10, ...)
```

~===~

## Some problems don't fit well into collections

~~~

### Dask Delayed

- Tool for creating arbitrary task graphs
- Dead simple interface (one function)
- Plays well with existing code (with some caveats)


```python
# Wrap functions to make them lazy
delayed(function)(*args, **kwargs) -> Delayed

# Wrap data to make attribute access lazy
delayed(data) -> Delayed
```

~~~

### Dask Delayed

```python
_
```

---

```python
results = {}

for a in A:
    for b in B:
        results[a, b] = fit(a, b)

best = score(results)
_
```

~~~

### Dask Delayed

```python
from dask import delayed, compute
```

---

```python
results = {}

for a in A:
    for b in B:
        results[a, b] = delayed(fit)(a, b)

best = delayed(score)(results)
result = best.compute()
```

~===~

### Collections author task graphs

<hr>

<img src="../images/grid_search_schedule.gif" width="100%">

<hr>

### Now we need to run them efficiently

~~~

### Dask schedulers target different architectures

---

### Easy swapping enables scaling up *and down*

~===~

### Single Machine Scheduler

- *Parallel CPU*: Uses multiple threads or processes

- *Minimizes RAM*: Choose tasks to remove intermediates

- *Low overhead:* ~100us per task

- *Concise*: ~600 LOC, stable for ~12 months

~===~

### Distributed Scheduler

- *Distributed*: One scheduler coordinates many workers

- *Data local*: Tries to moves computation to "best" worker

- *Asynchronous*: Continuous non-blocking conversation

- *Multi-user*: Several users can share the same system

- *HDFS Aware*: Works well with HDFS, S3, YARN, etc..

- *Less Concise*: ~3000 LOC Tornado TCP application

~~~

## Example

~~~

### Distributed Scheduler

<img src="../images/network-inverse.svg" width="80%">

~~~

### Task Scheduling

<img src="../images/fg-simple.svg">

    x = f(1)
    y = f(2)
    z = g(x, y)

<img src="../images/computer-tower.svg" width="15%">
<img src="../images/computer-tower.svg" width="15%">

~~~

### All decisions are done in-the-small (almost)

<img src="../images/svd-compressed.svg" width="60%">
<img src="../images/small-simple.svg" width="20%">

### All decisions are done in constant time (almost)

~~~

### Which function to run first?

<img src="../images/critical-path-1.svg">

~~~

### Prefer Tasks on Critical Path

<img src="../images/critical-path-2.svg">

~~~

### Which function to run first?

<img src="../images/expose-parallelism-1.svg">

~~~

### Expose Parallelism

<img src="../images/expose-parallelism-2.svg">

~~~

### Which function to run first?

<img src="../images/garbage-collection-1.svg">

~~~

### Release Data

<img src="../images/garbage-collection-2.svg">

~~~

### Release Data, free Memory

<img src="../images/garbage-collection-3.svg">

~~~

### Two Workers

<img src="../images/scheduling-workers-1.svg">

~~~

### Two Workers

<img src="../images/scheduling-workers-2.svg">

~~~

### Two Workers

<img src="../images/scheduling-workers-3.svg">

~~~

### Two Workers

<img src="../images/scheduling-workers-4.svg">

~~~

### Two Workers

<img src="../images/scheduling-workers-5.svg">

~~~

### Data Locality

<img src="../images/scheduling-workers-6.svg">

~~~

### Data Locality

<img src="../images/scheduling-workers-7.svg">

~~~

### Data Locality

<img src="../images/scheduling-workers-8.svg">

~~~

### .

<img src="../images/scheduling-workers-9.svg">

~~~

### Minimize Communication

<img src="../images/scheduling-workers-10.svg">

~~~

### Balance Computation and Communication

<img src="../images/scheduling-workers-12.svg">

~~~

### .

<img src="../images/scheduling-workers-13.svg">

~~~

### Work Steal

<img src="../images/scheduling-workers-14.svg">

~~~

### Work Steal

<img src="../images/scheduling-workers-15.svg">

~~~

### Other Optimizations ...

- Gracefully scale up or down based on load
- Optionally compress messages based on small samples
- Oversubscribe workers with many small tasks
- Batch many-small-messages in 2ms windows
- Spill unused data to disk

~===~

<img src="../images/gridsearch-lr.svg"
     align="right"
     width="20%">

## Dask is...

- *Familiar:* Implements NumPy/Pandas interfaces
- *Flexible:* for sophisticated and messy algorithms
- *Fast:* Optimized for demanding applications
- *Scales up:* Runs resiliently on clusters
- *Scales down:* Pragmatic on a laptop
- *Responsive:* for interactive computing

---

Dask *complements* the Python ecosystem.

~~~

### Easy to get started

conda/pip installable

```bash
$ conda install dask distributed -c conda-forge
$ pip install dask[complete] distributed --upgrade
```

---

```python
>>> from dask.distributed import Executor
>>> e = Executor()  # sets up local cluster
```

---

```bash
$ dask-scheduler

$ dask-worker scheduler-hostname:8786
$ dask-worker scheduler-hostname:8786
```

~~~

### Acknowledgements

- Countless [open source developers](https://github.com/dask/dask/graphs/contributors)
- SciPy developer community
- Continuum Analytics
- DARPA XData Program
- Moore Foundation

---

### Questions?

<img src="../images/grid_search_schedule.gif" width="100%">


~===~

## Extras...

~~~

### Q: How does Dask differ from Spark?

- Spark is great
    - ETL + Database operations
    - SQL-like streaming
    - Spark 2.0 is decently fast
    - Integrate with Java infrastructure
- Dask is great
    - Tight integration with NumPy, Pandas, Toolz, Sklearn, ...
    - Ad-hoc parallelism for custom algorithms
    - Easy deployment on clusters or laptops
    - Complement the existing SciPy ecosystem (Dask is lean)
- Both are great
    - Similar network designs and scalability limits
    - Decent Python APIs

~~~

### Q: How is dask used in practice?

- Large arrays for climate and atmospheric science (HDF5 data)
- Single machine lightweight PySpark clone for logs and JSON
- Dataframes on piles of CSV data
- Custom applications

---

- Roughly equal mix of academic/research and corporate
