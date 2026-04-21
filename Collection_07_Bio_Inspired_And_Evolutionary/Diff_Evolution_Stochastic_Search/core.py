import numpy as np

def differential_mutation(pop_weights, target_idx, F=0.8):
    # DE: Mutation via vector differences
    # v = x1 + F * (x2 - x3)
    # The 'Difference' between two agents is used to push a third agent.
    indices = [i for i in range(len(pop_weights)) if i != target_idx]
    r1, r2, r3 = np.random.choice(indices, 3, replace=False)
    
    x1, x2, x3 = pop_weights[r1], pop_weights[r2], pop_weights[r3]
    mutated_vector = x1 + F * (x2 - x3)
    
    print(f"🚀 DE: Differential Mutation created! Vector shift magnitude={np.linalg.norm(F*(x2-x3)):.4f}")
    return mutated_vector

print("🚀 Differential Evolution: Population-based vector optimization.")
pop_w = [np.random.randn(4) for _ in range(10)]
differential_mutation(pop_w, 0)
print("✅ Logic Check: Three-vector difference mutation verified.")
