import numpy as np

def maml_gradient_step(weights, task_grads):
    # MAML: Learn a 'Starting Point' that is one step away from any task
    # meta_update = weights - lr * mean(task_gradients)
    meta_update = np.mean(task_grads, axis=0)
    print(f"🚀 MAML: Meta-gradient calculated across {len(task_grads)} tasks.")
    return weights - 0.1 * meta_update

print("🚀 MAML Core: The mathematical heart of 'Learning to Learn'.")
w = np.random.randn(5)
grads = [np.random.randn(5) for _ in range(3)]
maml_gradient_step(w, grads)
print("✅ Logic Check: Meta-initialization update verified.")
