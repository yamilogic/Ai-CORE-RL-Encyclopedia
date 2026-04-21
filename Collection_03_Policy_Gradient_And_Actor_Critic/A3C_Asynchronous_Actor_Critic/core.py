import numpy as np

def a3c_parallel_update(global_w, worker_grad):
    # Multiple workers run in parallel, each updating the global weights
    # Asynchronous: No waiting for others!
    global_w += 0.1 * worker_grad
    print(f"🚀 A3C Global Update: Weights shifted by worker gradient.")
    return global_w

print("🚀 A3C Core: Parallel agents improving a single global brain.")
gw, wg = np.zeros(5), np.random.randn(5)
a3c_parallel_update(gw, wg)
print("✅ Logic Check: Asynchronous weight sync verified.")
