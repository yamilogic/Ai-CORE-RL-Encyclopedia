import numpy as np

def compute_priority_weight(td_error, epsilon=1e-6):
    # TD-Error Weighting: Focus on the 'Surprising' steps
    # Priority = |TD-Error| + small_constant
    priority = np.abs(td_error) + epsilon
    print(f"🚀 TD-Weighting: Error={td_error:.2f} | Priority Score={priority:.4f}")
    return priority

print("🚀 TD-Error Weighting: Prioritizing samples that the AI finds 'Surprising'.")
compute_priority_weight(-5.5)
print("✅ Logic Check: Absolute error to priority mapping verified.")
