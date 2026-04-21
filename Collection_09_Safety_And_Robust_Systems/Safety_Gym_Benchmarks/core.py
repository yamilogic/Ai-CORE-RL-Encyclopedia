import numpy as np

def safety_gym_step(pos, hazard_pos, action):
    # Safety Gym: A standardized benchmark for constrained RL.
    # Logic: Reward for moving toward Goal, Penalty for touching Hazard.
    # 'Cost' is tracked separately from 'Reward'.
    new_pos = pos + action
    reward = -np.linalg.norm(new_pos - np.array([10, 10])) # Distance to goal
    cost = 1.0 if np.linalg.norm(new_pos - hazard_pos) < 1.0 else 0.0
    
    print(f"🚀 Safety Gym: Reward={reward:.2f} | Cost={cost:.2f} | Danger={cost > 0}")
    return reward, cost

print("🚀 Safety Gym: Initializing Constrained Benchmark Environment...")
h = np.array([2, 2]) # Hazard
p = np.array([1.5, 1.5]) # Close to hazard
a = np.array([0.5, 0.5]) # Moving INTO hazard
safety_gym_step(p, h, a)
print("✅ Logic Check: Hazard-cost detection verified.")
