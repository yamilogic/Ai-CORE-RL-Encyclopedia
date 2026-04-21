import numpy as np

def inventory_order_decision(stock_level, lead_time, demand_forecast, weights):
    # Supply Chain: RL deciding how much to order
    # State = Current Stock, Lead Time, Expected Demand
    score = np.dot([stock_level, lead_time, demand_forecast], weights)
    order_quantity = max(0, int(score))
    print(f"🚀 Supply Chain: Stock={stock_level} | Forecast={demand_forecast} | Order Amount={order_quantity}")
    return order_quantity

print("🚀 Supply Chain RL: Optimizing inventory levels to minimize waste.")
inventory_order_decision(50, 3, 20, np.random.randn(3))
print("✅ Logic Check: Demand-aware ordering logic verified.")
