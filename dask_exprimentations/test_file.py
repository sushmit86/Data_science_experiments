import time
import ray
ray.init(num_cpus=13)

def f1():
    time.sleep(1)

@ray.remote
def f2():
    time.sleep(1)
start_time = time.time()
# The following takes ten seconds.
[f1() for _ in range(10)]
elapsed_time = time.time() - start_time
print('Time taken for step 1',elapsed_time)

# The following takes one second (assuming the system has at least ten CPUs).
start_time = time.time()
ray.get([f2.remote() for _ in range(100)])
elapsed_time = time.time() - start_time
print('Time taken for step 2',elapsed_time)
ray.shutdown()