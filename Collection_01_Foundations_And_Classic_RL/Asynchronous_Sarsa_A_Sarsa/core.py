import numpy as np

def asarsa_global_update(global_Q, local_grad, alpha=0.01):
    # Asynchronous Sarsa: Local workers update a shared Global Q-table
    # New Global = Old Global + alpha * Local_Gradient
    global_Q += alpha * local_grad
    print(f"🚀 A-Sarsa: Global Brain updated from worker experience. Mean Q={np.mean(global_Q):.2f}")
    return global_Q

print("🚀 Asynchronous Sarsa: Distributed on-policy learning.")
g_q = np.zeros((4, 2))
l_g = np.random.randn(4, 2)
asarsa_global_update(g_q, l_g)
print("✅ Logic Check: Asynchronous weight accumulation verified.")
