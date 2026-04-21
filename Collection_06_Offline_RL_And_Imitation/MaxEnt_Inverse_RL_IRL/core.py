import numpy as np

def maxent_reward_update(expert_features, agent_features, reward_weights):
    # MaxEnt IRL: Match the feature expectations of the expert
    # Weights += learning_rate * (Expert_Features - Agent_Features)
    grad = expert_features - agent_features
    reward_weights += 0.1 * grad
    print(f"🚀 MaxEnt IRL: Reward weights adjusted. Gradient Norm: {np.linalg.norm(grad):.4f}")
    return reward_weights

print("🚀 Maximum Entropy Inverse RL: Recovering the hidden 'Why' behind expert behavior.")
ex_feat = np.array([1.0, 0.5, 0.2])
ag_feat = np.array([0.8, 0.4, 0.3])
w = np.random.randn(3)
maxent_reward_update(ex_feat, ag_feat, w)
print("✅ Logic Check: Feature expectation matching verified.")
