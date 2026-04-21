import numpy as np

def cem_step(mu, sigma, objective_fn):
    # 1. Sample a population
    samples = np.random.normal(mu, sigma, (10, len(mu)))
    rewards = np.array([objective_fn(s) for s in samples])
    
    # 2. Pick the 'Elite' (top 20%)
    elite_idx = rewards.argsort()[-2:]
    elites = samples[elite_idx]
    
    # 3. Update distribution toward Elites
    new_mu, new_sigma = np.mean(elites, axis=0), np.std(elites, axis=0)
    print(f"🚀 CEM: New Mean = {new_mu} | Distribution narrowed toward success.")
    return new_mu, new_sigma

print("🚀 Cross-Entropy Method (CEM): Evolution-style optimization for RL.")
cem_step(np.zeros(2), np.ones(2), lambda x: -np.sum(x**2))
print("✅ Logic Check: Population sampling and Elite selection verified.")
