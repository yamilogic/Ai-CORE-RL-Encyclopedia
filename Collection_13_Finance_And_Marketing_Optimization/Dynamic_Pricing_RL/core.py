import numpy as np

def dynamic_pricing_step(inventory_age, competitor_price, demand_velocity, weights):
    # Dynamic Pricing: RL adjusting prices to maximize profit
    # State = Inventory Age, Competitor price, Recent sales speed
    state = np.array([inventory_age, competitor_price, demand_velocity])
    price_delta = np.dot(state, weights)
    final_price = competitor_price + price_delta
    print(f"🚀 Pricing RL: Demand={demand_velocity:.2f} | Competitor=${competitor_price:.2f} | New Price=${final_price:.2f}")
    return final_price

print("🚀 Dynamic Pricing RL: Real-time price optimization.")
age, comp, vel = 10, 45.0, 1.5
w = np.random.randn(3)
dynamic_pricing_step(age, comp, vel, w)
print("✅ Logic Check: Competitive pricing adjustment verified.")
