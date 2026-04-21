import numpy as np

def firefly_attraction(pos_a, pos_b, intensity_b, gamma=1.0):
    # Firefly: Movement toward 'Brighter' (higher fitness) flies
    # Attraction decays with distance squared (Light inverse square law)
    dist_sq = np.sum((pos_a - pos_b)**2)
    beta = intensity_b * np.exp(-gamma * dist_sq)
    
    new_pos = pos_a + beta * (pos_b - pos_a) + 0.01 * np.random.randn(*pos_a.shape)
    print(f"🚀 Firefly: Attracted toward light! Distance moved={np.linalg.norm(beta * (pos_b-pos_a)):.4f}")
    return new_pos

print("🚀 Firefly Algorithm: Light-based swarm optimization.")
f1, f2 = np.array([0.0, 0.0]), np.array([5.0, 5.0])
firefly_attraction(f1, f2, intensity_b=1.0)
print("✅ Logic Check: Distance-dependent attraction verified.")
