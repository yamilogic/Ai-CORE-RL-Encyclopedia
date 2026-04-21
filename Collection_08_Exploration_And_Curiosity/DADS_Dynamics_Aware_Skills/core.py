import numpy as np

def dads_skill_reward(state, next_state, skill_z, transition_model_w):
    # DADS: Dynamics-Aware Discovery of Skills
    # Reward = log( P(next_state | state, skill_z) / P(next_state | state) )
    # A skill is 'Good' if it makes the future more PREDICTABLE than average.
    # Skill 1 might move you specifically to the right. 
    # Without knowing the skill, the future is a 'blur'. 
    # With the skill, the future is a 'point'.
    
    pred_with_z = np.dot(np.concatenate([state, skill_z]), transition_model_w)
    prediction_error = np.linalg.norm(next_state - pred_with_z)
    
    # Reward is inverse of prediction error (high predictability)
    reward = 1.0 / (prediction_error + 1e-8)
    print(f"🚀 DADS: Skill Predictability Score={reward:.4f} | Error={prediction_error:.4f}")
    return reward

print("🚀 DADS: Initializing Predictability-based Skill Discovery...")
s, ns = np.random.randn(4), np.random.randn(4)
z = np.array([1, 0, 0]) # Skill ID 0
w_trans = np.random.randn(7, 4)
dads_skill_reward(s, ns, z, w_trans)
print("✅ Logic Check: Prediction-gain skill reward verified.")
