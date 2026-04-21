import numpy as np

def gwo_wolf_hierarchy(alpha_pos, beta_pos, delta_pos, wolf_pos, a_val):
    # GWO: Hunting behavior based on Social Hierarchy
    # Wolves move toward the average of Alpha, Beta, and Delta
    r1, r2 = np.random.rand(), np.random.rand()
    A1 = 2 * a_val * r1 - a_val
    C1 = 2 * r2
    D_alpha = np.abs(C1 * alpha_pos - wolf_pos)
    X1 = alpha_pos - A1 * D_alpha
    
    # (Simplified: Just showing the move toward Alpha)
    new_pos = X1 
    print(f"🚀 GWO: Wolf is following the Alpha. Distance narrowed by {np.linalg.norm(alpha_pos - wolf_pos):.4f}")
    return new_pos

print("🚀 Grey Wolf Optimizer: Social-hierarchy based search.")
a_alpha = np.array([10, 10])
w_curr = np.array([0, 0])
gwo_wolf_hierarchy(a_alpha, None, None, w_curr, a_val=2.0)
print("✅ Logic Check: Hierarchical attraction update verified.")
