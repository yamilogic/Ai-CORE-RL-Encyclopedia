import numpy as np

def curiosity_reward(s, ns, model):
    pred_ns = np.dot(s, model) # Simple world model
    error = np.mean(np.square(ns - pred_ns))
    return error # Higher error = Higher Curiosity Reward

print("🚀 Curiosity-Driven RL: Exploration via Prediction Error.")
s, ns = np.random.randn(4), np.random.randn(4)
model = np.random.randn(4, 4)
reward = curiosity_reward(s, ns, model)
print(f"✅ Intrinsic Reward: {reward:.4f}")
print("Logic: If the agent can't predict the next state, it becomes 'Curious' and explores.")
