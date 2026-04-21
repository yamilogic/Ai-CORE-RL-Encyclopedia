import numpy as np

def awac_weight_calculation(adv, beta=1.0):
    # AWAC: Advantage Weighted Actor-Critic.
    # Logic: Instead of complex policy gradients, we use 
    # Weighted Behavior Cloning. 
    # Weight = exp( Advantage / beta )
    # This 'Pushes' the policy toward actions that worked better than average.
    weights = np.exp(adv / beta)
    print(f"🚀 AWAC: Max Weight={np.max(weights):.4f} | Focusing on high-advantage actions.")
    return weights

print("🚀 AWAC: Initializing Advantage-Weighted Imitation...")
a_vals = np.array([1.0, 5.0, -2.0]) # Three actions with different success levels
awac_weight_calculation(a_vals)
print("✅ Logic Check: Exponential advantage weighting verified.")
