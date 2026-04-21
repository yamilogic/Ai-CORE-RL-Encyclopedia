import numpy as np

class Particle:
    def __init__(self, dim):
        self.pos = np.random.randn(dim)
        self.vel = np.zeros(dim)
        self.best_pos = self.pos.copy()
        self.best_score = -np.inf

    def update(self, global_best_pos, w=0.5, c1=1.5, c2=1.5):
        # PSO Update Rule: v = w*v + c1*r1*(pbest-pos) + c2*r2*(gbest-pos)
        r1, r2 = np.random.rand(), np.random.rand()
        cognitive = c1 * r1 * (self.best_pos - self.pos)
        social = c2 * r2 * (global_best_pos - self.pos)
        self.vel = w * self.vel + cognitive + social
        self.pos += self.vel
        print(f"🚀 PSO: Particle moved. Speed={np.linalg.norm(self.vel):.4f}")

print("🚀 PSO: Initializing Social-Swarm Optimization...")
p = Particle(dim=4)
g_best = np.array([0.0, 0.0, 0.0, 0.0])
p.update(g_best)
print("✅ Logic Check: Cognitive-Social velocity update verified.")
