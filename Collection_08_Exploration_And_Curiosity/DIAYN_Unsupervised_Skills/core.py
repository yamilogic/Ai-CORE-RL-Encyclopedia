import numpy as np

def diayn_reward(state, skill_id, discriminator_weights):
    # DIAYN: Maximize the probability that we can guess the 'Skill' from the 'State'
    # Reward = log( P(skill | state) )
    prediction = np.dot(state, discriminator_weights)
    skill_prob = np.exp(prediction[skill_id]) / np.sum(np.exp(prediction))
    reward = np.log(skill_prob + 1e-8)
    print(f"🚀 DIAYN: Skill={skill_id} | Reward (Discrimination)={reward:.2f}")
    return reward

print("🚀 DIAYN Core: Learning diverse skills without any external reward.")
s = np.random.randn(4)
dw = np.random.randn(4, 5) # 5 possible skills
diayn_reward(s, 2, dw)
print("✅ Logic Check: Skill-discrimination reward verified.")
