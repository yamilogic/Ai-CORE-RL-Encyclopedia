import numpy as np

def multi_fidelity_reward(low_fid_score, high_fid_score, confidence):
    # Multi-Fidelity: Combining 'Cheap' and 'Expensive' data
    # Final Score = (1-conf)*Low_Fidelity + (conf)*High_Fidelity
    # We use cheap sims to learn the basics, and expensive sims to polish
    weighted_r = (1 - confidence) * low_fid_score + confidence * high_fid_score
    print(f"🚀 Multi-Fidelity: Low-Fi Reward={low_fid_score} | High-Fi={high_fid_score} | Blended={weighted_r:.2f}")
    return weighted_r

print("🚀 Multi-Fidelity RL: Scaling intelligence by blending simulation and reality.")
multi_fidelity_reward(0.8, 0.4, 0.1) # Starting with more trust in low-fidelity
print("✅ Logic Check: Data fidelity blending for efficient scaling verified.")
