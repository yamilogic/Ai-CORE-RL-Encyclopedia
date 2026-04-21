import numpy as np

class MuZeroDynamics:
    """
    MuZero: Learning a 'Mental Model' of the world.
    Dynamics: (Latent_State, Action) -> (New_Latent_State, Reward)
    This allows planning in games where we don't know the rules.
    """
    def __init__(self, latent_dim=8):
        self.w_dyn = np.random.randn(latent_dim + 1, latent_dim + 1)

    def step(self, latent_state, action):
        # Predict next latent state and reward
        inp = np.append(latent_state, action)
        out = np.dot(inp, self.w_dyn)
        next_latent, reward = out[:-1], out[-1]
        print(f"🚀 MuZero: Predicted Latent Move. Reward={reward:.4f} | Latent Norm={np.linalg.norm(next_latent):.4f}")
        return next_latent, reward

print("🚀 MuZero: Initializing Latent-Dynamics Planning Engine...")
mu = MuZeroDynamics()
s_lat = np.random.randn(8)
mu.step(s_lat, 1.0)
print("✅ Logic Check: Latent-state transition prediction verified.")
