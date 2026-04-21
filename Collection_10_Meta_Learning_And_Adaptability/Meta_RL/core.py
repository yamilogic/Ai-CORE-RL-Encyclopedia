import numpy as np

def meta_update(theta, task_gradients):
    # theta: meta-parameters (knowledge across all tasks)
    # Task gradients: How to solve specific task A, B, C
    meta_grad = np.mean(task_gradients, axis=0)
    theta += 0.1 * meta_grad # Update meta-policy
    return theta

print("🚀 Meta-RL Core: 'Learning to Learn' across multiple tasks.")
theta = np.random.randn(5)
task_grads = [np.random.randn(5) for _ in range(3)]
new_theta = meta_update(theta, task_grads)
print(f"✅ Meta-Policy Updated: {new_theta[:3]}...")
print("Logic: The agent adjusts its starting weights to be good at everything.")
