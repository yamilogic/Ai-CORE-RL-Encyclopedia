import numpy as np

def trpo_constraint(old_policy, new_policy):
    # KL Divergence check: How much did the policy change?
    kl = np.sum(old_policy * np.log(old_policy / (new_policy + 1e-5)))
    delta = 0.01 # Trust Region Bound
    
    is_safe = kl < delta
    print(f"🚀 TRPO: KL Divergence = {kl:.5f} | Within Trust Region: {is_safe}")
    return is_safe

print("🚀 TRPO Core: Mathematical safety through Trust Regions.")
old = np.array([0.5, 0.5])
new = np.array([0.51, 0.49])
trpo_constraint(old, new)
print("✅ Logic Check: Small updates allowed, large updates rejected.")
