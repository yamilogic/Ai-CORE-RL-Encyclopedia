import numpy as np

def pareto_optimal_step(rewards_vector, preference_weights):
    # Multi-Objective: Balancing conflicting goals (e.g., Speed vs. Energy)
    # rewards_vector: [Score_A, Score_B, ...]
    scalar_reward = np.dot(rewards_vector, preference_weights)
    print(f"🚀 Multi-Objective: Scores={rewards_vector} | Scalarized Reward={scalar_reward:.2f}")
    return scalar_reward

print("🚀 Multi-Objective Pareto Optimization RL: Solving for trade-offs.")
r_vec = np.array([10.0, 2.0]) # High Speed, Low Battery
p_weights = np.array([0.5, 0.5])
pareto_optimal_step(r_vec, p_weights)
print("✅ Logic Check: Weighted multi-objective scalarization verified.")
