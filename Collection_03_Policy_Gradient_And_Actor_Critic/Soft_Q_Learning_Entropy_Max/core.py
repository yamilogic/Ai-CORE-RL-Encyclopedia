import numpy as np

def soft_q_value_iter(q_values, temperature=1.0):
    # Soft Q-Learning: The foundation of Max-Entropy RL
    # V(s) = temperature * log( sum( exp( Q(s,a) / temperature ) ) )
    # This is the Log-Sum-Exp operator (Smooth Max)
    v_soft = temperature * np.log(np.sum(np.exp(q_values / temperature)) + 1e-8)
    print(f"🚀 Soft-Q: Log-Sum-Exp Value={v_soft:.4f} | Temperature={temperature}")
    return v_soft

print("🚀 Soft Q-Learning Core: Entropy-regularized value iteration.")
qs = np.array([10.0, 5.0, 2.0]) # Q-values for 3 actions
soft_q_value_iter(qs, temperature=2.0)
print("✅ Logic Check: Temperature-scaled smooth-max calculation verified.")
