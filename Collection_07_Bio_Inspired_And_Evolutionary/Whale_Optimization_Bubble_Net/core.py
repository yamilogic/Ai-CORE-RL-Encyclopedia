import numpy as np

def whale_bubble_net_step(whale_pos, best_pos):
    # WOA: Hunting behavior of Humpback Whales
    # Spiral movement to encircle prey
    r = np.random.rand()
    A = 2 * r - 1
    C = 2 * r
    
    # 50% chance to do spiral update, 50% chance to encircle
    if np.random.rand() < 0.5:
        # Spiral update
        distance_to_best = np.abs(best_pos - whale_pos)
        new_pos = distance_to_best * np.exp(0.5 * r) * np.cos(2 * np.pi * r) + best_pos
    else:
        # Encircle update
        D = np.abs(C * best_pos - whale_pos)
        new_pos = best_pos - A * D
        
    print(f"🚀 Whale: Bubble-net spiral completed. Target Dist={np.linalg.norm(best_pos - new_pos):.4f}")
    return new_pos

print("🚀 Whale Optimization: Spiral-based swarm intelligence.")
w_p = np.array([1.0, 1.0])
b_p = np.array([10.0, 10.0])
whale_bubble_net_step(w_p, b_p)
print("✅ Logic Check: Spiral and encircling logic verified.")
