## Dask-Gateway

<img src="../images/dask_icon.svg" width=20%>

Jim Crist

<hr width=40%>

*Anaconda Inc.*


~===~

## Dask Deployment Options

- Kubernetes: [`dask-kubernetes`](https://kubernetes.dask.org/)
- YARN: [`dask-yarn`](https://yarn.dask.org/)
- HPC Clusters: [`dask-jobqueue`](https://jobqueue.dask.org/en/latest/)

~~~

## Usage

**Kubernetes**

```python
>>> from dask_kubenetes import KubeCluster
>>> cluster = KubeCluster(...)
```

**YARN**

```python
>>> from dask_yarn import YarnCluster
>>> cluster = YarnCluster(...)
```

**HPC Clusters**

```python
>>> from dask_jobqueue import PBSCluster
>>> cluster = PBSCluster(...)
```

~~~

#### These options work great for many users...

---

#### but lack some features institutions might expect.

~~~

## A few common requests

- Central Management
- Restrict user permissions, resources
- Proxy out network connections
- Support long running clusters
- Encryption and authentication

~===~

## Dask-Gateway

~~~

### "Like JupyterHub, but for Dask"

~~~

## Architecture

<img src="../images/dask-gateway-architecture.svg" width=80%>

~~~

## Highlights

- **Centrally Managed**: Admins do the heavy lifting, users get easy cluster
  access.

- **Secure by default**: Automatic TLS everywhere, pluggable authentication model.

- **Flexible**: Configurable backends, natively supports Kubernetes,
  Hadoop/YARN, and HPC Job Queues.

- **Robust to Failure**: can be restarted or failover without losing existing
  clusters.

~===~

## Docs!

~~~

## Mostly undocumented!

~~~

https://jcrist.github.io/dask-gateway/

~===~

### Could this be useful for you?

---

###I'd love to get in contact:

- Twitter: [@jiminy_crist](https://twitter.com/jiminy_crist)

- Github: [jcrist](https://github.com/jcrist)
