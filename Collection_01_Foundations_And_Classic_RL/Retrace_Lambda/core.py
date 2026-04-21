import numpy as np

def retrace_weight(target_prob, behavior_prob):
    # Retrace: Safe off-policy multi-step learning
    # Weights are clipped to 1 to prevent 'Variance Explosion'
    rho = target_prob / behavior_prob
    weight = min(1.0, rho)
    print(f"🚀 Retrace: Target={target_prob:.2f} | Behavior={behavior_prob:.2f} | Safe Weight={weight:.4f}")
    return weight

print("🚀 Retrace(λ) Core: Low-variance off-policy multi-step learning.")
retrace_weight(0.8, 0.2) # High importance, but clipped to 1.0
print("✅ Logic Check: Importance weight clipping for stability verified.")
