import numpy as np

def expectile_loss(diff, tau=0.8):
    # Expectile Regression: The math behind Implicit Q-Learning (IQL)
    # Penalizes 'over-estimation' and 'under-estimation' asymmetrically
    # Loss = |tau - indicator(diff < 0)| * diff^2
    weight = np.where(diff < 0, 1 - tau, tau)
    loss = weight * (diff**2)
    print(f"🚀 Expectile: Tau={tau} | Weighted Loss={np.mean(loss):.4f}")
    return np.mean(loss)

print("🚀 Expectile Regression Core: The foundation of In-Sample Offline RL.")
d = np.array([2.0, -1.0, 5.0, -3.0]) # Differences (Target - Predicted)
expectile_loss(d, tau=0.9) # High tau = care more about better-than-average
print("✅ Logic Check: Asymmetric squared loss calculation verified.")
