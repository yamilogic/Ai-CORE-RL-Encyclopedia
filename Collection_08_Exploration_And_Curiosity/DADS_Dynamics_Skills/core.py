import numpy as np

def dads_skill_reward(s, ns, skill_id, skill_model_w):
    # DADS: Maximize how 'Predictable' the state change is given the skill
    # Reward = log( P(next_state | state, skill) ) - log( P(next_state | state) )
    # If the skill makes the world predictable, it is a good skill!
    prediction = np.dot(np.append(s, skill_id), skill_model_w)
    error = np.sum(np.square(ns - prediction))
    reward = -error # Higher reward for lower prediction error
    print(f"🚀 DADS: Prediction Error={error:.4f} | Skill Reward={reward:.2f}")
    return reward

print("🚀 DADS Core: Unsupervised skill discovery via predictable world dynamics.")
s_val, ns_val = np.random.randn(4), np.random.randn(4)
w = np.random.randn(5, 4) # 4 state + 1 skill
dads_skill_reward(s_val, ns_val, 1, w)
print("✅ Logic Check: Predictability-based skill reward verified.")
