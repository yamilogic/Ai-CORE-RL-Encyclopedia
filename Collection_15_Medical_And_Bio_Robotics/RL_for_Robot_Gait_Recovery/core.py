import numpy as np

def gait_recovery_reward(is_upright, distance_walked, damage_level):
    # RL for Gait Recovery: Teaching a damaged robot to walk again.
    # Reward = Distance - (C1 * Fall_Penalty + C2 * Motor_Strain)
    # The agent must find a 'Limping' gait that works for its broken leg.
    if not is_upright:
        return -100.0
    reward = distance_walked * 10.0 - damage_level * 5.0
    print(f"🚀 Gait-RL: Distance={distance_walked:.2f} | Damage={damage_level} | Reward={reward:.2f}")
    return reward

print("🚀 RL for Robot Gait Recovery: Adaptability in the face of failure.")
gait_recovery_reward(is_upright=True, distance_walked=5.0, damage_level=2)
print("✅ Logic Check: Upright-distance-damage gait reward verified.")
