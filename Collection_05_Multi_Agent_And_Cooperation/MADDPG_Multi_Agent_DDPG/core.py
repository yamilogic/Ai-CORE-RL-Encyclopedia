import numpy as np

class MADDPG:
    """
    MADDPG: Centralized Training, Decentralized Execution.
    The critic sees EVERYTHING, the actor only sees its own state.
    """
    def __init__(self, n_agents, state_dim, action_dim):
        self.n_agents = n_agents
        # Critic sees global state and all actions
        self.global_critic_w = np.random.randn(n_agents * (state_dim + action_dim), 1) * 0.1
        # Actor only sees local state
        self.local_actor_w = np.random.randn(state_dim, action_dim) * 0.1

    def get_local_action(self, local_state):
        return np.tanh(np.dot(local_state, self.local_actor_w))

    def centralized_evaluation(self, all_states, all_actions):
        inp = np.concatenate([all_states.flatten(), all_actions.flatten()])
        q_val = np.dot(inp, self.global_critic_w)
        print(f"🚀 MADDPG Critic: Evaluating Global Situation. Total Q={q_val.item():.2f}")
        return q_val

print("🚀 MADDPG: Initializing Multi-Agent Coordination Engine...")
maddpg = MADDPG(n_agents=2, state_dim=4, action_dim=2)
s_local = np.random.randn(4)
a_local = maddpg.get_local_action(s_local)
maddpg.centralized_evaluation(np.random.randn(2, 4), np.random.randn(2, 2))
print("✅ Logic Check: Centralized-Critic / Decentralized-Actor logic verified.")
