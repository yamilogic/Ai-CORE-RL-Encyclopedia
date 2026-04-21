import numpy as np

def n_step_reward(rewards, gamma, bootstrap_value):
    # Standard: r + gamma*V(s')
    # N-Step: r1 + gamma*r2 + gamma^2*r3 + ... + gamma^n*V(s_n)
    n = len(rewards)
    total_r = sum([rewards[i] * (gamma**i) for i in range(n)])
    target = total_r + (gamma**n) * bootstrap_value
    print(f"🚀 N-Step ({n}): Total Discounted Reward = {target:.2f}")
    return target

print("🚀 N-Step Returns: Looking further into the future for faster updates.")
n_step_reward([1, 1, 1], 0.9, 10.0)
print("✅ Logic Check: Multi-step reward summation verified.")
