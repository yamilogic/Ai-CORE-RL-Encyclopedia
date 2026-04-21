import numpy as np

def safe_step(s, a, safety_limit=0.5):
    reward = 10.0 # Goal
    # Constraint: Agent must not exceed safety_limit
    constraint_violation = np.abs(a) > safety_limit
    
    if constraint_violation:
        reward = -50.0 # Heavy penalty for safety breach
        print("⚠️ SAFETY BREACH: Action rejected, emergency stop!")
    return reward

print("🚀 Safe RL Core: Constrained Optimization for Real-world safety.")
r = safe_step(None, 0.7) # Unsafe action
r2 = safe_step(None, 0.2) # Safe action
print(f"✅ Rewards: Unsafe={r} | Safe={r2}")
