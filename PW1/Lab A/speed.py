import time
from decay import simulate, simulate_loop
start = time.perf_counter()
simulate_loop(200000, 0.4)
end = time.perf_counter()
loop_time = end-start

start = time.perf_counter()
simulate(200000, 0.4)
end = time.perf_counter()
numpy_time = end-start
speedup = loop_time / numpy_time
print(f"Loop time: {loop_time:.4f}")
print(f"NumPy time: {numpy_time:.4f}")
print(f"NumPy is {speedup:.1f}x faster than Loop time.")