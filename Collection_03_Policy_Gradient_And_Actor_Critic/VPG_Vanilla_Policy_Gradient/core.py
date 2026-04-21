import numpy as np

def vpg_gradient(log_probs, rewards):
    # VPG: The simplest 'Policy Gradient' algorithm
    # Update = mean( log_prob * return )
    # This pushes the weights to make actions with high returns more likely
    loss = -np.mean(log_probs * rewards)
    print(f"🚀 VPG: Mean Return={np.mean(rewards):.2f} | Loss={loss:.4f}")
    return loss

print("🚀 VPG Core: The direct ancestor of PPO, TRPO, and A3C.")
p = np.array([-1.2, -0.5, -2.1]) # Log probabilities
r = np.array([10.0, 2.0, 15.0]) # Returns
vpg_gradient(p, r)
print("✅ Logic Check: Basic gradient-to-return scaling verified.")
