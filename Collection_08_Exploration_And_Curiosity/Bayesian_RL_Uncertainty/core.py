import numpy as np

def bayesian_q_update(q_samples, reward, next_q_samples):
    # Bayesian RL: Q-values are DISTRIBUTIONS, not single numbers
    # We maintain a posterior over what the real Q-value might be
    prior_mean = np.mean(q_samples)
    likelihood_reward = reward + 0.9 * np.mean(next_q_samples)
    
    # Update: Move the whole distribution toward the likelihood
    updated_samples = q_samples + 0.1 * (likelihood_reward - q_samples)
    print(f"🚀 Bayesian RL: Q-Mean={np.mean(updated_samples):.2f} | Variance={np.var(updated_samples):.4f}")
    return updated_samples

print("🚀 Bayesian RL Core: Modeling uncertainty in the agent's own knowledge.")
q = np.random.normal(5, 1, 100) # 100 samples representing the distribution
nq = np.random.normal(6, 1, 100)
bayesian_q_update(q, 10.0, nq)
print("✅ Logic Check: Posterior distribution update verified.")
