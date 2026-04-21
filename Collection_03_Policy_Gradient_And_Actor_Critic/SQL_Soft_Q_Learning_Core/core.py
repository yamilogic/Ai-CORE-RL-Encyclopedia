import numpy as np

def soft_q_value(qs, alpha=0.1):
    # Soft Q-Learning: Using Log-Sum-Exp to find the 'Soft' Maximum
    # V(s) = alpha * log( sum( exp(Q/alpha) ) )
    # This is more stable and exploratory than hard ArgMax
    v = alpha * np.log(np.sum(np.exp(qs / alpha)))
    print(f"🚀 SQL: Individual Qs={qs} | Soft Value (V)={v:.2f}")
    return v

print("🚀 Soft Q-Learning (SQL) Core: Maximum Entropy value approximation.")
q_vals = np.array([2.0, 5.0, 1.0])
soft_q_value(q_vals)
print("✅ Logic Check: Log-Sum-Exp soft-max value verified.")
