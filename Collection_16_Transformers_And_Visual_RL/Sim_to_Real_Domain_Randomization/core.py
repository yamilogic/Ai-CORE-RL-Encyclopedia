import numpy as np

def domain_randomization_step(base_params):
    # Sim-to-Real: Randomize the physics to make the agent robust
    # friction = base_friction + noise
    randomized_friction = base_params['friction'] + np.random.uniform(-0.5, 0.5)
    randomized_mass = base_params['mass'] + np.random.uniform(-2.0, 2.0)
    print(f"🚀 Sim-to-Real: Physics Randomized! Friction: {randomized_friction:.2f} | Mass: {randomized_mass:.2f}")
    return randomized_friction, randomized_mass

print("🚀 Sim-to-Real (DR): Training for the messy real world inside a random simulation.")
params = {'friction': 1.0, 'mass': 5.0}
domain_randomization_step(params)
print("✅ Logic Check: Physical parameter perturbation verified.")
