# Install Jupyter Lab
```sh
$ pip install jupyterlab
```

# Install Jupyter Lab Extention called: `Dask Labextension`
```sh
$ pip install dask-labextension
```

# Install Dask Job Queue for Connecting Dask Cluster
```sh
$ pip install dask-jobqueue
```

# Setting Up Schedular in Local Machine
```sh
$ dask-scheduler
```
## Note: Above command will spin up a scheduler running in your machine 
##       in a port
## Example logs: 
distributed.scheduler - INFO - Scheduler at: tcp://192.168.1.9:8786
distributed.scheduler - INFO - dashboard at:  192.168.1.9:8787
You can open the Dashboard to checkout the various statistics of the 
Scheduler and Workers


# Setting up Worker(s) and join to Scheduler using single command line
## You can open as many terminal and type below command
## You will get that many workers connected to the scheduler
```sh
$ dask-worker tcp://192.168.1.9:8786
```


# Sample Python Code for Local Cluster, distributed accross workers
File name: test_dask_distributed.py
```py
import time

import dask.array as da
from dask.distributed import Client, LocalCluster

t1 = time.time()
x = da.random.random((42000, 40000), chunks=(1000, 1000))
y = da.exp(x).sum()

# If you do `y.compute()` it will execute on the syngle machine by utilizing #multiple VCPUs or multiple cores


if __name__ == '__main__':
    cluster = LocalCluster("192.168.1.9:6786")
    client = Client(cluster)
    # But if you want to submit/compute this task/statement to the cluster so that #all workers could take/divide processes 
    c = client.submit(y.compute)
    client.gather(c)
    print(f"Execution took: {time.time() - t1} seconds...")
```

# My findings till now:
Need to find further evidence that the above local cluster is deviding 
work accross multiple worker nodes. 
Right now, I could only see the CPU spikes > 100% accrocs all VCPUs.
There are no logs in running Worker terminal logs.