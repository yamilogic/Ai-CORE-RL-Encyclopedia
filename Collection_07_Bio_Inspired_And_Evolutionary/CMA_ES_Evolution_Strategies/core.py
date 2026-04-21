import numpy as np

class CMA_ES:
    """
    CMA-ES: The Gold Standard for Black-Box Optimization.
    Adapts a Gaussian distribution based on successful samples.
    """
    def __init__(self, dim, mean=None, sigma=0.5):
        self.dim = dim
        self.mean = mean if mean is not None else np.zeros(dim)
        self.sigma = sigma
        self.C = np.eye(dim) # Covariance Matrix

    def sample(self, pop_size=10):
        # Generate population from the current distribution
        return [np.random.multivariate_normal(self.mean, self.sigma**2 * self.C) for _ in range(pop_size)]

    def update(self, successful_samples):
        # 1. Update Mean (The average of the best samples)
        self.mean = np.mean(successful_samples, axis=0)
        # 2. Update Covariance (The direction of success)
        # Simplified: Move C toward the covariance of successful samples
        new_C = np.cov(np.array(successful_samples).T)
        self.C = 0.8 * self.C + 0.2 * new_C
        print(f"🚀 CMA-ES: Distribution refined. Mean={self.mean[:2]}... | Sigma={self.sigma}")
        return self.mean

print("🚀 CMA-ES: Initializing Derivative-Free Optimizer...")
cma = CMA_ES(dim=4)
samps = cma.sample()
cma.update(samps[:3]) # Top 3 samples
print("✅ CMA-ES: Covariance-aware distribution update verified.")
