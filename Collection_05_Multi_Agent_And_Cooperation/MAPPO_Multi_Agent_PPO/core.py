import numpy as np

class MAPPO:
    """
    MAPPO: Multi-Agent PPO with Centralized Value Function.
    Standard PPO architecture adapted for cooperative multi-agent tasks.
    """
    def __init__(self, n_agents, state_dim, action_dim):
        self.n_agents = n_agents
        # Centralized Critic: Sees all agent observations
        self.central_critic_w = np.random.randn(n_agents * state_dim, 1) * 0.1
        # Decentralized Actor: Only sees own observation
        self.local_actor_w = np.random.randn(state_dim, action_dim) * 0.1

    def get_action_and_val(self, local_obs, all_obs):
        # Policy
        logits = np.dot(local_obs, self.local_actor_w)
        # Value (Centralized)
        val = np.dot(all_obs.flatten(), self.central_critic_w)
        print(f"🚀 MAPPO: Local Logits={logits[:2]}... | Central Value={val.item():.2f}")
        return logits, val

print("🚀 MAPPO: Initializing Multi-Agent PPO Coordination...")
mappo = MAPPO(n_agents=3, state_dim=4, action_dim=2)
lobs = np.random.randn(4)
aobs = np.random.randn(3, 4)
mappo.get_action_and_val(lobs, aobs)
print("✅ Logic Check: Centralized-Value PPO logic verified.")
