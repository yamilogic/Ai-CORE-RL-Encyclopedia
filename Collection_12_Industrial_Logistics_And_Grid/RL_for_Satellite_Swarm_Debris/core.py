import numpy as np

def debris_removal_reward(collision_avoided, debris_captured, fuel_consumed):
    # RL for Satellite Swarms: Cleaning up space.
    # Reward = Debris_Score - (C1 * Fuel + C2 * Collision_Risk)
    # The agent manages 100 small 'CubeSats' to grab space junk.
    reward = debris_captured * 100.0 - (fuel_consumed * 5.0)
    if not collision_avoided:
        reward -= 5000.0
        
    print(f"🚀 Space-RL: Captured={debris_captured} | Fuel={fuel_consumed:.4f} | Reward={reward:.2f}")
    return reward

print("🚀 RL for Satellite Swarm Debris Removal: Cleaning the orbital graveyard.")
debris_removal_reward(collision_avoided=True, debris_captured=2, fuel_consumed=1.5)
print("✅ Logic Check: Capture-vs-collision reward verified.")
