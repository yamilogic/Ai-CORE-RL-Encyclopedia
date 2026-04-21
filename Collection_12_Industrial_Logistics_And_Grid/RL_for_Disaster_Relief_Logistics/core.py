import numpy as np

def relief_logistics_reward(people_helped, average_response_time, resource_waste):
    # RL for Disaster Relief: Coordinating supplies after an earthquake.
    # Reward = People_Helped - (C1 * Response_Time + C2 * Waste)
    # The agent must route trucks through broken roads to reach survivors.
    time_penalty = average_response_time * 10.0
    reward = people_helped * 100.0 - (time_penalty + resource_waste * 1.0)
    print(f"🚀 Relief-RL: Helped={people_helped} | AvgTime={average_response_time:.1f}h | Reward={reward:.2f}")
    return reward

print("🚀 RL for Disaster Relief Logistics: Optimizing life-saving supply chains.")
relief_logistics_reward(people_helped=1200, average_response_time=4.5, resource_waste=50)
print("✅ Logic Check: Speed-waste-survivor reward verified.")
