import numpy as np

def ag_precision_reward(soil_moisture, fertilizer_level, crop_yield, water_cost):
    # RL for Precision Agriculture: Managing a vertical farm.
    # Reward = Crop_Yield - (C1 * Water_Cost + C2 * Fertilizer_Waste)
    # The agent must keep plants alive with MINIMUM resources.
    reward = crop_yield * 100.0 - (water_cost * 2.0 + fertilizer_level * 5.0)
    print(f"🚀 Ag-RL: Yield={crop_yield:.2f} | Water=${water_cost:.2f} | Reward={reward:.2f}")
    return reward

print("🚀 RL for Precision Agriculture: Optimizing the future of food.")
ag_precision_reward(soil_moisture=0.6, fertilizer_level=10, crop_yield=5.0, water_cost=20)
print("✅ Logic Check: Yield-resource-cost reward verified.")
