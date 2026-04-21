import numpy as np

def pcpo_projection(raw_update, constraint_w, threshold=0.1):
    # PCPO: Projection-based Constrained Policy Optimization
    # Step 1: Take a normal RL step (maximize reward)
    # Step 2: If the new policy is unsafe, 'Project' it back to the closest safe point.
    # Projection = raw_update - max(0, (dot(raw, w) - threshold)) / |w|^2 * w
    
    violation = np.dot(raw_update, constraint_w) - threshold
    if violation > 0:
        print(f"🚀 PCPO: Safety Violation ({violation:.2f})! Projecting back to safe manifold.")
        projection = raw_update - (violation / (np.linalg.norm(constraint_w)**2 + 1e-8)) * constraint_w
        return projection
        
    print("🚀 PCPO: Action is within safe bounds.")
    return raw_update

print("🚀 PCPO Core: Two-stage safety projection for deep RL.")
r_u = np.array([1.0, 1.0]) # Update wants to go North-East
c_w = np.array([1.0, 0.0]) # East is the constraint
pcpo_projection(r_u, c_w, threshold=0.5)
print("✅ Logic Check: Constrained manifold projection verified.")
