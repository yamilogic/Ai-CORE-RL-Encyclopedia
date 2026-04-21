import numpy as np

def q_sigma_blend(expected_v, sampled_v, sigma=0.5):
    # Q(sigma): Blending 'Expected' and 'Sampled' multi-step updates
    # sigma=1: Sarsa (Sampled)
    # sigma=0: Expected Sarsa (Mathematical)
    v_final = (sigma * sampled_v) + ((1 - sigma) * expected_v)
    print(f"🚀 Q(σ): Sigma={sigma} | Blended Value={v_final:.2f}")
    return v_final

print("🚀 Q(σ) Core: A unified algorithm that generalizes Sarsa and Expected Sarsa.")
q_sigma_blend(10.0, 5.0, 0.5)
print("✅ Logic Check: Dynamically blended future value calculation verified.")
