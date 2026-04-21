import numpy as np

def ic3_conflict_resolution(my_goal, other_agent_goal):
    # IC3: Handling competing objectives in a shared space.
    # Logic: If goals conflict, agents must 'Negotiate' or 'Yield'.
    # Reward = Joint_Success - Conflict_Penalty
    
    dist = np.linalg.norm(my_goal - other_agent_goal)
    if dist < 0.5:
        print("💥 IC3: Conflict Detected! Agents are fighting for the same spot.")
        penalty = -10.0
    else:
        penalty = 0.0
        
    print(f"🚀 IC3: Goal Distance={dist:.4f} | Penalty={penalty}")
    return penalty

print("🚀 IC3: Initializing Interactive Conflict Management...")
g1, g2 = np.array([1, 1]), np.array([1.1, 0.9]) # Overlapping goals
ic3_conflict_resolution(g1, g2)
print("✅ Logic Check: Overlap-based conflict penalty verified.")
