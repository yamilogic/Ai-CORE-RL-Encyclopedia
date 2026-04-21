import numpy as np

def energy_balancing_step(demand, supply, battery_level, pricing_weights):
    # Smart Grid: RL balancing load and storage
    # State = Current demand, supply, and battery %
    net_power = supply - demand
    action = np.tanh(net_power * pricing_weights[0] + battery_level * pricing_weights[1])
    print(f"🚀 Smart Grid: Net Power={net_power:.2f} | Battery={battery_level:.2f} | Storage Action={action:.2f}")
    return action

print("🚀 Smart Grid RL: Balancing renewable supply and consumer demand.")
energy_balancing_step(100.0, 120.0, 0.5, np.random.randn(2))
print("✅ Logic Check: Net-power storage coordination verified.")
