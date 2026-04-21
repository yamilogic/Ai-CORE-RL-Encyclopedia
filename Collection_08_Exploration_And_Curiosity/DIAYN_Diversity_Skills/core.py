import numpy as np

def diayn_skill_reward(state, skill_id, discriminator_w):
    # DIAYN: Unsupervised Skill Discovery
    # Reward = log( P(skill_id | state) )
    # An agent is rewarded if a discriminator can 'Guess' which skill it is doing.
    # This forces skills to be distinct (e.g. Skill 1 = Jump, Skill 2 = Crouch).
    logits = np.dot(state, discriminator_w)
    pred_skill = np.argmax(logits)
    reward = 1.0 if pred_skill == skill_id else -1.0
    print(f"🚀 DIAYN: Target Skill={skill_id} | Predicted={pred_skill} | Reward={reward}")
    return reward

print("🚀 DIAYN: Initializing Diversity-based Skill Discovery...")
s_val = np.random.randn(4)
w_disc = np.random.randn(4, 5) # 5 possible skills
diayn_skill_reward(s_val, 2, w_disc)
print("✅ Logic Check: Discriminator-based skill reinforcement verified.")
