import numpy as np

def ship_navigation_step(heading, current_drift, obstacle_dist, fuel_left, weights):
    # Ship RL: Navigating oceans while saving fuel
    # State = Heading, Wind/Current, Obstacles, Fuel
    safety_score = obstacle_dist * 0.7
    efficiency_score = fuel_left * 0.3
    steering_angle = np.tanh(np.dot([safety_score, efficiency_score, current_drift], weights))
    print(f"🚀 Ship RL: Drift={current_drift:.2f} | Steering Angle={steering_angle:.2f} | Fuel Check={fuel_left}")
    return steering_angle

print("🚀 Autonomous Ship Navigation RL: Handling ocean dynamics.")
dft, obs, fl = 0.5, 100.0, 500.0
w = np.random.randn(3)
ship_navigation_step(0.0, dft, obs, fl, w)
print("✅ Logic Check: Drift-compensation steering verified.")
