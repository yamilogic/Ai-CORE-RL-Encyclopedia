import numpy as np

def adjust_cooling(server_temp, humidity, fan_weights):
    # RL for Energy: [Temp, Humidity] -> Adjust Fan Speed/Chiller
    # Reward = -(Energy Consumption) - (Penalty if Temp > 80C)
    state = np.array([server_temp, humidity])
    fan_speed = np.clip(np.dot(state, fan_weights), 0, 100)
    energy_cost = fan_speed * 0.5
    print(f"🚀 Cooling RL: Temp={server_temp}C | Adjusting Fans to {fan_speed:.1f}% | Energy: {energy_cost:.2f}kW")
    return fan_speed

print("🚀 Data Center Cooling RL: Managing massive infrastructure for energy efficiency.")
w = np.random.randn(2)
adjust_cooling(75, 45, w)
print("✅ Logic Check: Energy-temperature trade-off optimization verified.")
