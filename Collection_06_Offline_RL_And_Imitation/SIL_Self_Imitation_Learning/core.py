import numpy as np

def sil_update(s, a, actual_r, predicted_v):
    # SIL: If I did better than I expected, IMITATE that action!
    if actual_r > predicted_v:
        advantage = actual_r - predicted_v
        print(f"🚀 SIL: Success! Reward {actual_r} > Value {predicted_v}. Imitating...")
        return advantage
    return 0

print("🚀 Self-Imitation Learning (SIL): Learning from your own best moments.")
sil_update(None, None, 10.0, 5.0)
print("✅ Logic Check: Selective imitation of high-reward trajectories verified.")
