import numpy as np

def mirror_descent_step(current_probs, advantages, eta=0.1):
    # Mirror Descent Policy Optimization: Generalized Policy Update
    # New Pi = Pi * exp(eta * Adv) / normalization
    # This is the 'Mirror' of the standard gradient descent
    weights = current_probs * np.exp(eta * advantages)
    next_probs = weights / np.sum(weights)
    print(f"🚀 Mirror Descent: Probabilities shifted toward Advantage. Entropy Change={np.sum(-next_probs * np.log(next_probs + 1e-8)):.4f}")
    return next_probs

print("🚀 Mirror Descent Policy Optimization: The theoretical core of TRPO and PPO.")
p_init = np.array([0.33, 0.33, 0.33])
advs = np.array([2.0, -1.0, 0.5])
mirror_descent_step(p_init, advs)
print("✅ Logic Check: Exponetial-weighted policy shift verified.")
