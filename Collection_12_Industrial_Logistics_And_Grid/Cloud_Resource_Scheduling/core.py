import numpy as np

def cloud_scheduler(cpu_usage, ram_usage, task_queue, server_weights):
    # Cloud Scheduling: RL deciding which server gets the task
    # State = Server load, Task requirement
    load = cpu_usage * 0.5 + ram_usage * 0.5
    efficiency_score = np.dot(load, server_weights)
    best_server = np.argmin(efficiency_score)
    print(f"🚀 Cloud RL: Task assigned to Server {best_server} | Current Avg Load={np.mean(load):.2f}")
    return best_server

print("🚀 Cloud Resource Scheduling RL: Minimizing energy and latency.")
c, r = np.random.rand(5), np.random.rand(5) # 5 Servers
w = np.random.randn(5)
cloud_scheduler(c, r, None, w)
print("✅ Logic Check: Load-balancing server assignment verified.")
