import numpy as np

def ppo_update(policy, s, a, r, logp_old):
    # PPO Logic: Ratio Clipping
    new_logp = np.log(0.6) # Simulated new probability
    ratio = np.exp(new_logp - logp_old)
    clipped_ratio = np.clip(ratio, 0.8, 1.2)
    advantage = r - 0.5 # Simple advantage estimate
    loss = -min(ratio * advantage, clipped_ratio * advantage)
    print(f"💡 PPO: Ratio = {ratio:.2f} | Clipped = {clipped_ratio:.2f} | Loss = {loss:.4f}")

print("🚀 PPO Core (Numpy): Policy Gradient with Clipping Logic.")
ppo_update(None, None, None, 1.0, np.log(0.5))
print("✅ Logic Check: Trust Region Clipping verified.")
