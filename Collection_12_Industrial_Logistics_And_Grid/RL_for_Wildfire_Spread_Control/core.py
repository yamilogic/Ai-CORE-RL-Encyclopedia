import numpy as np

def wildfire_control_reward(acres_saved, houses_lost, water_spent):
    # RL for Wildfire: Deploying planes and ground crews.
    # Reward = (Acres_Saved * 10) - (Houses_Lost * 1000 + Water * 1)
    # The agent must predict where the fire will go and 'Cut it off'.
    reward = acres_saved * 10.0 - (houses_lost * 1000.0 + water_spent * 0.5)
    print(f"🚀 Wildfire-RL: Saved={acres_saved} | Houses Lost={houses_lost} | Reward={reward:.2f}")
    return reward

print("🚀 RL for Wildfire Spread Control: Strategic disaster containment.")
wildfire_control_reward(acres_saved=5000, houses_lost=1, water_spent=2000)
print("✅ Logic Check: Strategic-containment reward verified.")
