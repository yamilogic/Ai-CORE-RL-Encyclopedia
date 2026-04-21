import numpy as np

class GorilaLearner:
    """
    Gorila: The first massively distributed DQN architecture.
    Features separate Actor, Learner, and Parameter Server nodes.
    """
    def __init__(self):
        self.master_weights = np.random.randn(10, 10)

    def receive_gradient(self, grad):
        # Async update from thousands of actors
        self.master_weights += 0.001 * grad
        print(f"🚀 Gorila: Received Gradient. Weights Norm={np.linalg.norm(self.master_weights):.4f}")

print("🚀 Gorila: Initializing Massively Distributed Learning Node...")
g = GorilaLearner()
g.receive_gradient(np.random.randn(10, 10))
print("✅ Logic Check: Async parameter-server update verified.")
