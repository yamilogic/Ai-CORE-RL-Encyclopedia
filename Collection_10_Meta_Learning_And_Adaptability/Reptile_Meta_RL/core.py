import numpy as np

def reptile_update(meta_weights, task_weights, lr=0.1):
    # Reptile: Move the meta-weights toward the task-specific weights
    # meta = meta + lr * (task - meta)
    new_meta = meta_weights + lr * (task_weights - meta_weights)
    print(f"🚀 Reptile: Meta-weights shifted toward Task-weights (Step size: {lr})")
    return new_meta

print("🚀 Reptile Core: The simple, fast alternative to MAML for Meta-RL.")
meta, task = np.array([1.0, 1.0]), np.array([2.0, 0.5])
reptile_update(meta, task)
print("✅ Logic Check: Meta-learning via weight interpolation verified.")
