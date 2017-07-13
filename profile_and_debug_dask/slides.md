### Make it Work, Make it Right, Make it Fast

### Debugging and Profiling in Dask

<img src="../images/dask_icon.svg" width=20%>

Jim Crist

Continuum Analytics

<hr width=40%>

*SciPy 2017*

~===~

## What is Dask???

- A parallel computing framework

- Written in pure Python

- That leverages the excellent Python ecosystem

- Using blocked algorithms and task scheduling

~===~

## Dask strives to be easy to use

~~~

### Write Familiar Python Code

```python
from dask_searchcv import GridSearchCV

search = GridSearchCV(estimator, grid)
search.fit(X, y)
```

~~~

### Task Graph is Generated Behind the Scenes

<img src="../images/grid_search_schedule-0.png" width="100%">

~~~

### Dask Schedulers Execute the Graph in Parallel

<img src="../images/grid_search_schedule.gif" width="100%">

~===~

## This talk is about what to do when things don't work right

~===~

## Examples

~===~

# Summary

~~~

- *Think* about your problem
    - May be a better algorithm
    - Maximize parallelism
    - Minimize Intermediate data size

~~~

- Think about when to call `compute`
- Use `dask.compute` to compute multiple values at once

~~~

- Use `dask.visualize` to inspect graphs

~~~

- Profile!
- `snakeviz` or `line_profiler` for task level profiling
- `dask.diagnostics` or `dask.distributed` dashboard for parallel profiling

~~~

- Debug locally
- PDB works fine with dask

~~~

- Scale out *if needed*
- Use `persist` to store intermediates in memory
    - Just as with `compute`, want to do this intelligently
- Use the diagnostics page

~===~

### Acknowledgements

- Countless open source developers
- SciPy developer community
- Gordon & Betty Moore Foundation
- DARPA XData Program
- Continuum Analytics

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

~~~

### Q: How is dask used in practice?

- Large arrays for climate and atmospheric science (HDF5 data)
- Single machine lightweight PySpark clone for logs and JSON
- Dataframes on piles of CSV data
- Custom applications

---

- Roughly equal mix of academic/research and corporate
