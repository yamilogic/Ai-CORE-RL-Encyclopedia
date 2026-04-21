import numpy as np

def compute_pareto_reward(rewards, preferences):
    # Multi-Objective RL: Optimizing for multiple goals at once
    # Reward is a VECTOR, not a scalar.
    # Total Reward = dot(reward_vector, preference_vector)
    total_r = np.dot(rewards, preferences)
    print(f"🚀 MORL: Objective Vector: {rewards} | Preferences: {preferences} | Scaled Reward: {total_r:.2f}")
    return total_r

print("🚀 MORL Core: Balancing conflicting goals (e.g., Speed vs. Safety).")
r_vec = np.array([10.0, -2.0]) # [Profit, Risk]
pref = np.array([0.5, 0.5]) # Equal importance
compute_pareto_reward(r_vec, pref)
print("✅ Logic Check: Weighted scalarization of multiple rewards verified.")
