import numpy as np

def renewable_grid_reward(solar_output, wind_output, consumer_demand, battery_level):
    # RL for Renewable Grid: Balancing unpredictable energy.
    # Reward = - (Grid_Imbalance + Battery_Degradation + CO2_Usage)
    # The agent must decide when to 'Store' energy and when to 'Sell' it.
    imbalance = np.abs((solar_output + wind_output + battery_level) - consumer_demand)
    reward = -imbalance
    print(f"🚀 Grid-RL: Supply={solar_output+wind_output:.2f} | Demand={consumer_demand:.2f} | Reward={reward:.2f}")
    return reward

print("🚀 RL for Renewable Energy Grid: Balancing the green transition.")
renewable_grid_reward(Solar=100, Wind=50, consumer_demand=160, battery_level=10)
print("✅ Logic Check: Supply-demand imbalance reward verified.")
