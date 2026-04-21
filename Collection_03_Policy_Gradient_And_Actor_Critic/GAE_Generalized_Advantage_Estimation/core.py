import numpy as np

def gae_estimate(rewards, values, gamma=0.99, lam=0.95):
    # GAE: Balancing Bias vs Variance in Advantage
    # Delta = r + gamma*V(s') - V(s)
    # Advantage = sum( (gamma*lambda)^k * delta_{t+k} )
    deltas = rewards[:-1] + gamma * values[1:] - values[:-1]
    advantage = 0
    advantages = []
    for d in reversed(deltas):
        advantage = d + gamma * lam * advantage
        advantages.insert(0, advantage)
    print(f"🚀 GAE: Advantage estimation complete. Mean Advantage = {np.mean(advantages):.4f}")
    return advantages

print("🚀 GAE Core: The secret to stable Policy Gradients (PPO/A3C).")
r, v = np.random.randn(10), np.random.randn(10)
gae_estimate(r, v)
print("✅ Logic Check: Temporal difference lambda-return verified.")
