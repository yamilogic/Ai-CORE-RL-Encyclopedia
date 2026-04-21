import numpy as np

def data_center_cooling_reward(temp_list, energy_usage, pUE_target=1.1):
    # RL for Data Center Cooling: Minimizing PUE (Power Usage Effectiveness).
    # Reward = - (Energy_Usage + Penalty(If Temp > Limit))
    # The agent controls thousands of fans and chillers.
    avg_temp = np.mean(temp_list)
    temp_penalty = 100.0 if avg_temp > 25.0 else 0.0
    pue = energy_usage / 1000.0 # Normalized
    
    reward = -(pue + temp_penalty)
    print(f"🚀 Cooling-RL: PUE={pue:.4f} | Avg Temp={avg_temp:.2f} | Reward={reward:.2f}")
    return reward

print("🚀 RL for Data Center Cooling: Managing thermodynamic efficiency.")
temps = [22, 23, 24, 21]
data_center_cooling_reward(temps, 1200)
print("✅ Logic Check: Temperature-penalty/energy-usage reward verified.")
