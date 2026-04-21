import numpy as np

def objective(w):
    return -np.sum(np.square(w - 5)) # Goal: Weights should be 5

def train_es():
    w = np.zeros(3)
    lr, sigma, n_pop = 0.1, 0.1, 20
    
    for i in range(100):
        noise = np.random.randn(n_pop, 3)
        rewards = np.array([objective(w + sigma * n) for n in noise])
        std_rewards = (rewards - np.mean(rewards)) / (np.std(rewards) + 1e-5)
        w += lr / (n_pop * sigma) * np.dot(noise.T, std_rewards)
        if i % 20 == 0: print(f"Iteration {i} | Best Weights: {w}")
    return w

print("🚀 Evolution Strategies: Optimizing weights without gradients...")
train_es()
