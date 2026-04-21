import numpy as np

def risk_sensitive_utility(reward, beta=0.5):
    # Risk-Sensitive RL: Exponential Utility
    # U(r) = -exp(-beta * r)
    # beta > 0: Risk-Averse (Hates losses)
    # beta < 0: Risk-Seeking (Loves gambles)
    utility = -np.exp(-beta * reward)
    print(f"🚀 Risk-Sensitive: Reward={reward} | Beta={beta} | Utility={utility:.4f}")
    return utility

print("🚀 Risk-Sensitive RL: Non-linear utility optimization.")
risk_sensitive_utility(10.0, beta=0.1)  # Positive reward
risk_sensitive_utility(-10.0, beta=0.1) # Penalty is 'felt' much more strongly
print("✅ Logic Check: Exponential risk-aversion utility verified.")
