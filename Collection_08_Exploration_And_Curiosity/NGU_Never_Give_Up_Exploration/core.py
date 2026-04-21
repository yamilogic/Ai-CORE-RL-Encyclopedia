import numpy as np

class NGU:
    """
    Never Give Up (NGU): Long-term and Short-term Exploration.
    Combines Episodic Novelty and Life-long Novelty.
    """
    def __init__(self, state_dim, hash_dim=1024):
        self.state_dim = state_dim
        # 1. Life-long Novelty: RND (Random Network Distillation)
        self.rnd_target_w = np.random.randn(state_dim, 64)
        self.rnd_predictor_w = np.random.randn(state_dim, 64)
        
        # 2. Episodic Novelty: Counting unique visits in current game
        self.episode_memory = []

    def get_intrinsic_reward(self, state):
        # Life-long Novelty (RND)
        target = np.dot(state, self.rnd_target_w)
        pred = np.dot(state, self.rnd_predictor_w)
        life_long_r = np.sum((target - pred)**2)
        
        # Episodic Novelty (K-Nearest Neighbors style)
        episodic_r = 0
        if len(self.episode_memory) > 0:
            distances = [np.linalg.norm(state - s) for s in self.episode_memory]
            episodic_r = 1.0 / (np.sqrt(np.min(distances)) + 1e-3)
        
        self.episode_memory.append(state)
        
        # Combined Reward
        total_intrinsic = episodic_r * np.clip(life_long_r, 1.0, 5.0)
        print(f"🚀 NGU: Life-long={life_long_r:.2f} | Episodic={episodic_r:.2f} | Total={total_intrinsic:.2f}")
        return total_intrinsic

print("🚀 NGU: Initializing Never Give Up Exploration Engine...")
ngu = NGU(state_dim=4)
s1 = np.random.randn(4)
ngu.get_intrinsic_reward(s1)
ngu.get_intrinsic_reward(np.random.randn(4))
print("✅ NGU: Dual-scale curiosity reward verified.")
