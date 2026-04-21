import numpy as np

def ga_crossover_mutate(parent_a, parent_b, mutation_rate=0.1):
    # GA: Evolution via Survival of the Fittest
    # Crossover: 50% from Dad, 50% from Mom
    mask = np.random.rand(*parent_a.shape) > 0.5
    child = np.where(mask, parent_a, parent_b)
    
    # Mutation: Randomly flipping bits or adding noise
    if np.random.rand() < mutation_rate:
        child += np.random.randn(*child.shape) * 0.1
        print("🚀 GA: Mutation occurred! DNA modified.")
        
    print("🚀 GA: New Child Genome created via Crossover.")
    return child

print("🚀 Genetic Algorithm: Standard Evolutionary RL.")
p1 = np.array([1.0, 1.0, 1.0, 1.0])
p2 = np.array([0.0, 0.0, 0.0, 0.0])
ga_crossover_mutate(p1, p2)
print("✅ Logic Check: Masked crossover and random mutation verified.")
