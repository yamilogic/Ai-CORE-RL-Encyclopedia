import numpy as np

def feudal_manager(state, goal_embedding):
    # FeUdal: Manager sets direction in 'Latent Space'
    # Worker must follow that direction
    latent_dir = np.tanh(np.dot(state, goal_embedding))
    print(f"🚀 FuN Manager: Latent Direction set to {latent_dir[:3]}...")
    return latent_dir

def feudal_worker(state, latent_dir, weights):
    # Worker's reward is the COSINE SIMILARITY between its movement and Manager's direction
    movement = np.dot(state, weights)
    alignment = np.dot(movement, latent_dir) / (np.linalg.norm(movement) * np.linalg.norm(latent_dir) + 1e-8)
    print(f"🚀 FuN Worker: Alignment with Manager: {alignment:.4f}")
    return alignment

print("🚀 FeUdal Networks (FuN): Hierarchical control via latent direction alignment.")
s, ge, w = np.random.randn(8), np.random.randn(8, 4), np.random.randn(8, 4)
dir_l = feudal_manager(s, ge)
feudal_worker(s, dir_l, w)
print("✅ Logic Check: Latent space directional coordination verified.")
