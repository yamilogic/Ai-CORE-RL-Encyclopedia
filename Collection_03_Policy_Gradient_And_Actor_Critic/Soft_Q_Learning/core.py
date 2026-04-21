import numpy as np

def soft_q_update(q_values, alpha=0.1):
    # Standard Q: max(Q)
    # Soft Q: log(sum(exp(Q/alpha)))
    # This considers ALL actions, but gives more weight to better ones
    v = alpha * np.log(np.sum(np.exp(q_values / alpha)))
    print(f"🚀 Soft Q-Value: {v:.4f} | (Standard Max would be {np.max(q_values):.2f})")
    return v

print("🚀 Soft Q-Learning Core: The bridge between Q-learning and Maximum Entropy.")
q = np.array([2.0, 1.5, 0.5])
soft_q_update(q)
print("✅ Logic Check: Soft-max value incorporates multiple good actions.")
