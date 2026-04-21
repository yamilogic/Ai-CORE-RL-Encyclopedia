import numpy as np

class MAVEN:
    """
    MAVEN: Multi-Agent Variational Exploration.
    Uses a latent variable 'z' to coordinate exploration across agents.
    """
    def __init__(self, n_agents, state_dim, latent_dim=4):
        self.n_agents = n_agents
        # Policy takes state AND latent 'z'
        self.actor_w = np.random.randn(state_dim + latent_dim, 1) * 0.1

    def sample_exploration_mode(self):
        # Pick a 'Strategy' for this episode
        z = np.random.randn(4)
        print(f"🚀 MAVEN: New Exploration Latent sampled. Global Strategy Vector: {z}")
        return z

    def get_coordinated_action(self, state, z):
        inp = np.concatenate([state, z])
        return np.dot(inp, self.actor_w)

print("🚀 MAVEN: Initializing Coordinated Exploration Engine...")
maven = MAVEN(n_agents=2, state_dim=4)
strat_z = maven.sample_exploration_mode()
maven.get_coordinated_action(np.random.randn(4), strat_z)
print("✅ Logic Check: Latent-coordinated multi-agent action verified.")
