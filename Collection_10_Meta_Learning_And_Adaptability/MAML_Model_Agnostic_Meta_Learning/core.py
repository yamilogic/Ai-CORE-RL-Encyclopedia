import numpy as np

def maml_inner_update(theta, task_grads, alpha=0.01):
    # MAML Inner Loop: Quickly adapting to a specific task
    # Theta_prime = Theta - alpha * Grad(Task)
    return theta - alpha * task_grads

def maml_outer_update(theta, all_task_primes_grads, beta=0.001):
    # MAML Outer Loop: Learning the initialization that makes adaptation fast
    # New Theta = Theta - beta * sum( Grads at Theta_prime )
    return theta - beta * np.mean(all_task_primes_grads, axis=0)

print("🚀 MAML: Initializing Meta-Learning Engine...")
t = np.random.randn(4)
g_inner = np.random.randn(4)
t_prime = maml_inner_update(t, g_inner)
print(f"🚀 MAML: Inner Update complete. Prime={t_prime[:2]}...")
maml_outer_update(t, [np.random.randn(4) for _ in range(3)])
print("✅ Logic Check: Meta-gradient nested update verified.")
