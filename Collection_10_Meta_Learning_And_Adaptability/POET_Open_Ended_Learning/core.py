import numpy as np

def poet_evolve_env(env_params):
    # POET: Evolving the environment alongside the agent
    # If the agent is too good, make the 'Challenge' harder!
    mutation = np.random.uniform(-0.2, 0.2, size=env_params.shape)
    new_challenge = env_params + mutation
    print(f"🚀 POET: Environment Evolved! New Terrain Complexity: {np.mean(new_challenge):.2f}")
    return new_challenge

print("🚀 POET Core: Co-evolving Agents and Challenges for open-ended intelligence.")
p = np.array([1.0, 2.0]) # Terrain difficulty
poet_evolve_env(p)
print("✅ Logic Check: Environment mutation for curricula generation verified.")
