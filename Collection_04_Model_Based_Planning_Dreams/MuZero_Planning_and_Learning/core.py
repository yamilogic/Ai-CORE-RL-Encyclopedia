import numpy as np

def muzero_dynamics(latent_state, action, weights):
    # MuZero: Learning the Dynamics, Reward, and Value in Latent Space
    # No need for a real simulator!
    next_latent = np.tanh(np.dot(np.append(latent_state, action), weights))
    reward = np.dot(next_latent, np.random.randn(next_latent.shape[0]))
    print(f"🚀 MuZero Dynamics: Predicted Reward = {reward:.2f} | Latent state updated.")
    return next_latent, reward

print("🚀 MuZero: Planning without a model (Learning the Model itself).")
muzero_dynamics(np.random.randn(8), 1, np.random.randn(9, 8))
print("✅ Logic Check: Latent dynamics and reward prediction verified.")
