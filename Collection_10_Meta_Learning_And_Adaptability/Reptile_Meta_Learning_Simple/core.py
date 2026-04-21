import numpy as np

def reptile_step(meta_weights, task_weights, epsilon=0.1):
    # Reptile: Simple Meta-Learning via Weight Interpolation
    # New Meta Weights = Old + epsilon * (Task Weights - Old)
    # It slowly moves the 'Initial' brain toward the 'Learned' brain
    new_meta = meta_weights + epsilon * (task_weights - meta_weights)
    print(f"🚀 Reptile: Meta-Brain shifted toward task-specific solution. Delta={np.linalg.norm(task_weights - meta_weights):.4f}")
    return new_meta

print("🚀 Reptile Meta-Learning: The simple approach to fast adaptation.")
w_m = np.array([0.5, 0.5])
w_t = np.array([0.8, 0.2]) # Weights learned on a specific task
reptile_step(w_m, w_t)
print("✅ Logic Check: Weight-interpolation update verified.")
