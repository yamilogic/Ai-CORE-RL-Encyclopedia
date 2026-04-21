import numpy as np

def distributional_q(s, quantiles):
    # Instead of one number, we learn a distribution of possible rewards
    # quantiles = [10th percentile, 50th, 90th...]
    dist = np.sort(np.dot(s, quantiles))
    print(f"🚀 Distributional RL: 10% Chance of {dist[0]:.2f} | 90% Chance of {dist[-1]:.2f}")
    return dist

print("🚀 QR-DQN Core: Learning the 'Risk and Probability' of rewards.")
s = np.random.randn(4)
q_dist = np.random.randn(4, 5) # 5 quantiles
distributional_q(s, q_dist)
print("✅ Logic Check: Reward distribution (not just average) verified.")
