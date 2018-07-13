## Running Python on Apache YARN

---

## It's a thing!

Jim Crist

~===~

## What is Apache YARN???

- The resource manager for scheduling applications on Hadoop clusters

- Manages memory and cpu usage across the cluster

- Written in Java

- Not easy to use if you're not writing Java

- Also not easy to use if you're writing Java

~===~

## Difficulties with deploying Python on YARN

- Hadoop security is complicated

- Java only tooling

- File distribution, can't just pip/conda install

~===~

# :(

~===~

## But... Things are better now!

~===~

# New tools!

---

### Maybe they're useful to you?

- [`conda-pack`](https://conda.github.io/conda-pack/): Package conda environments for redistribution

- [`skein`](https://jcrist.github.io/skein/): Schedule and manage yarn applications

- [`dask-yarn`](http://dask-yarn.readthedocs.io/): Run dask on YARN

- [`hadoop-test-cluster`](https://github.com/jcrist/hadoop-test-cluster): Test your code against a realistic hadoop cluster

~===~

## Examples

~===~

## Remote Jupyter Kernel

~===~

## Dask on YARN

~===~

### Do you use the Hadoop ecosystem?

### Could this be useful for you?

---

###I'd love to get in contact:

- Twitter: [@jiminy_crist](https://twitter.com/jiminy_crist)

- Github: [jcrist](https://github.com/jcrist)
