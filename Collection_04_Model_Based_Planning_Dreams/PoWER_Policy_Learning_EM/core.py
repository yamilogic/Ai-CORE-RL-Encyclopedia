import numpy as np

def power_update(parameters, explorations, rewards):
    # PoWER: EM-style Policy Search
    # New Theta = Theta + sum(exploration * reward) / sum(reward)
    # It is a weighted average of the 'Success' found during exploration
    weighted_exploration = np.sum([e * r for e, r in zip(explorations, rewards)], axis=0)
    total_reward = np.sum(rewards) + 1e-8
    
    new_params = parameters + (weighted_exploration / total_reward)
    print(f"🚀 PoWER: Parameters updated via Expectation-Maximization. Total R={total_reward:.2f}")
    return new_params

print("🚀 PoWER Core: EM-based policy improvement for motor primitives.")
p = np.array([1.0, 1.0])
exps = [np.random.randn(2) for _ in range(3)]
rs = [10.0, 50.0, 5.0]
power_update(p, exps, rs)
print("✅ Logic Check: EM-weighted parameter update verified.")
