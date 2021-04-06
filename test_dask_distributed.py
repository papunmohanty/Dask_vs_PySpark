import time

import dask.array as da
from dask.distributed import Client, LocalCluster

t1 = time.time()
x = da.random.random((42000, 40000), chunks=(100, 100))
y = da.exp(x).sum()

# If you do `y.compute()` it will execute on the syngle machine by utilizing #multiple VCPUs or multiple cores

if __name__ == "__main__":
    cluster = LocalCluster("192.168.1.9:6786")
    client = Client(cluster)
    # But if you want to submit/compute this task/statement to the cluster so that #all workers could take/divide processes 
    c = client.submit(y.compute)
    client.gather(c)
    print(f"Execution took: {time.time() - t1} seconds...")
