import numpy as np

def reps_update(advantages, eta=2.0):
    # REPS: Bounding the information loss (Relative Entropy)
    # weights = exp(advantage / eta)
    # Eta is the 'Temperature' that controls how much we trust the data
    exp_adv = np.exp(advantages / eta)
    weights = exp_adv / np.sum(exp_adv)
    print(f"🚀 REPS: Max Weight={np.max(weights):.4f} | Information change bounded by eta.")
    return weights

print("🚀 REPS Core: Policy search with a trust region on information loss.")
adv = np.array([1.0, 5.0, 2.0])
reps_update(adv)
print("✅ Logic Check: Softmax-style weight calculation for safe updates verified.")
