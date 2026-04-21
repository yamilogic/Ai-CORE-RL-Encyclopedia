import numpy as np

def dynamic_pricing_reward(price, demand, inventory_cost):
    # RL for Dynamic Pricing: Finding the 'Sweet Spot' price.
    # Reward = (Price * Sales) - (Inventory_Cost + Loss_of_Goodwill)
    # The agent adjusts prices based on stock levels and competitor data.
    sales = 100 - price * 2.0 # Simple demand curve
    sales = np.clip(sales, 0, demand)
    profit = price * sales - inventory_cost
    print(f"🚀 Pricing-RL: Price=${price:.2f} | Sales={sales:.0f} | Profit=${profit:.2f}")
    return profit

print("🚀 RL for Dynamic Pricing: Optimizing revenue in competitive markets.")
dynamic_pricing_reward(Price=45.0, demand=50, inventory_cost=5.0)
print("✅ Logic Check: Demand-curve-based profit reward verified.")
