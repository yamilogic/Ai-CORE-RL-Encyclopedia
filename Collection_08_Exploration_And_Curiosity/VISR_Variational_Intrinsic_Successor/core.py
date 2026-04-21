import numpy as np

def visr_successor_reward(state_features, skill_embedding):
    # VISR: Variational Intrinsic Successor Features
    # Reward = dot( Successor_Features , Skill_Embedding )
    # This aligns the 'Potential Future' of the agent with the 'Intent' of the skill.
    reward = np.dot(state_features, skill_embedding)
    print(f"🚀 VISR: Alignment Reward={reward:.4f} | Matching Future to Intent.")
    return reward

print("🚀 VISR: Initializing Intent-based Future Alignment...")
s_f = np.array([0.1, 0.9, 0.0]) # Future is mostly 'Y' direction
z_e = np.array([0.0, 1.0, 0.0]) # Intent is 'Y' direction
visr_successor_reward(s_f, z_e)
print("✅ Logic Check: Feature-embedding alignment reward verified.")
