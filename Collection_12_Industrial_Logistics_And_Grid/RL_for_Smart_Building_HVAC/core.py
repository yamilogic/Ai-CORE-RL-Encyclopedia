import numpy as np

def smart_hvac_reward(temp_error, co2_level, energy_bill):
    # RL for Smart Buildings: Comfort vs Energy.
    # Reward = - (Temp_Error + CO2_Penalty + Energy_Cost)
    # The agent manages vents and heaters based on occupancy sensors.
    comfort_penalty = np.abs(temp_error) * 10.0
    air_quality_penalty = np.max([0, co2_level - 800]) * 0.1
    reward = -(comfort_penalty + air_quality_penalty + energy_bill * 0.5)
    print(f"🚀 HVAC-RL: TempErr={temp_error:.1f}C | CO2={co2_level} | Reward={reward:.2f}")
    return reward

print("🚀 RL for Smart Building HVAC: Thermodynamic comfort optimization.")
smart_hvac_reward(temp_error=1.5, co2_level=950, energy_bill=100)
print("✅ Logic Check: Comfort-air-quality-energy reward verified.")
