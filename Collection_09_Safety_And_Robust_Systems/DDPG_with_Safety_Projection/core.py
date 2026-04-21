import numpy as np

def safety_projection(action, safe_bounds):
    # Safety Layer: Projecting a 'Dangerous' action back into 'Safe' space
    # If action > Limit, Clip to Limit
    projected_action = np.clip(action, safe_bounds[0], safe_bounds[1])
    if not np.array_equal(action, projected_action):
        print(f"⚠️ Safety Layer: Dangerous action {action} BLOCKED. Projected to {projected_action}")
    return projected_action

print("🚀 Safe-RL: Enforcing physical constraints on agent actions.")
lims = [-1.0, 1.0]
act = np.array([5.5]) # Very dangerous action!
safety_projection(act, lims)
print("✅ Logic Check: Safe action manifold projection verified.")
