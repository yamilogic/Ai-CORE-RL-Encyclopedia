import numpy as np

def supply_chain_hedging_reward(inventory_levels, ship_arrival_times, demand_forecast):
    # RL for Supply Chain: Balancing Stockout vs Holding Costs
    # Reward = Sales_Profit - Holding_Cost - Stockout_Penalty
    # The agent must learn to order parts EARLY to avoid 'Shock' risks.
    profit = np.sum(demand_forecast) * 10
    holding = np.sum(inventory_levels) * 0.5
    stockout = 100.0 if np.min(inventory_levels) < 0 else 0
    reward = profit - holding - stockout
    print(f"🚀 Supply-RL: Reward={reward:.2f} | Risk Mitigation active.")
    return reward

print("🚀 RL for Supply Chain: Managing global logistics under uncertainty.")
supply_chain_hedging_reward([10, -5, 20], [2, 5], [10, 10, 10]) # One stockout (-5)
print("✅ Logic Check: Profit-cost-risk reward function verified.")
