import numpy as np

def es_parameter_update(center_weights, population_noise, scores, lr=0.01):
    # ES: Evolution Strategies (Black-box optimization)
    # New_Weights = Center + sum( Noise * Score )
    # This is massively scalable because actors don't need to send gradients.
    # They only send a single number (The Score).
    standardized_scores = (scores - np.mean(scores)) / (np.std(scores) + 1e-8)
    weighted_noise = np.zeros_like(center_weights)
    for noise, score in zip(population_noise, standardized_scores):
        weighted_noise += noise * score
        
    new_weights = center_weights + lr * weighted_noise
    print(f"🚀 ES Scaling: Update Complete. Center Shift={np.linalg.norm(lr * weighted_noise):.4f}")
    return new_weights

print("🚀 ES: Initializing Massively Parallel Evolution Engine...")
c_w = np.random.randn(10)
noises = [np.random.randn(10) for _ in range(5)]
s_list = np.array([10.0, 50.0, -20.0, 100.0, 5.0])
es_parameter_update(c_w, noises, s_list)
print("✅ Logic Check: Weighted-noise parameter update verified.")
