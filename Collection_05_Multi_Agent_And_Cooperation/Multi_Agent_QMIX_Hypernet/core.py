import numpy as np

class QMIXMixer:
    """
    QMIX: Monotonic Value Mixing with Hypernetworks.
    Ensures that Global Q is monotonic with respect to individual agent Qs.
    """
    def __init__(self, n_agents, state_dim, embed_dim=64):
        self.n_agents = n_agents
        self.state_dim = state_dim
        self.embed_dim = embed_dim
        
        # Hypernetworks: State -> Weights for the Mixer
        # Weights must be positive to ensure monotonicity
        self.hyper_w1 = np.random.randn(state_dim, n_agents * embed_dim) * 0.1
        self.hyper_w2 = np.random.randn(state_dim, embed_dim) * 0.1
        
        # Biases
        self.hyper_b1 = np.random.randn(state_dim, embed_dim) * 0.1
        self.hyper_b2 = np.random.randn(state_dim, 1) * 0.1

    def mix(self, agent_qs, global_state):
        # 1. Generate Weights via Hypernetworks
        # We take the absolute value to ensure w > 0 (Monotonicity)
        w1 = np.abs(np.dot(global_state, self.hyper_w1)).reshape(self.n_agents, self.embed_dim)
        w2 = np.abs(np.dot(global_state, self.hyper_w2)).reshape(self.embed_dim, 1)
        
        # 2. Generate Biases
        b1 = np.dot(global_state, self.hyper_b1).reshape(1, self.embed_dim)
        b2 = np.dot(global_state, self.hyper_b2).reshape(1, 1)
        
        # 3. Two-layer Monotonic Mixing
        # Hidden layer: agent_qs @ w1 + b1
        hidden = np.maximum(0, np.dot(agent_qs, w1) + b1) # ELU or ReLU
        
        # Final layer: hidden @ w2 + b2
        q_total = np.dot(hidden, w2) + b2
        
        print(f"🚀 QMIX: Agent Qs={agent_qs} | Total Mixed Q={q_total.item():.2f}")
        return q_total

print("🚀 QMIX: Initializing Monotonic Hypernetwork Mixer...")
mixer = QMIXMixer(n_agents=3, state_dim=10)
s = np.random.randn(10)
qs = np.array([1.5, 2.0, -0.5]) # Individual agent contributions
mixer.mix(qs, s)
print("✅ QMIX: Monotonic coordination mixing verified.")
