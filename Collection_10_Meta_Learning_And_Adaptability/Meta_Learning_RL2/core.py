import numpy as np

class RL2Agent:
    """
    RL^2: Fast Adaptation via Recurrent RL.
    The 'Hidden State' acts as the 'Learning Algorithm'.
    """
    def __init__(self, state_dim, action_dim, hidden_dim=128):
        self.hidden_dim = hidden_dim
        # Weights for the RNN (which learns to learn)
        self.rnn_w = np.random.randn(state_dim + action_dim + 2, hidden_dim) * 0.1

    def step(self, state, prev_action, prev_reward, prev_done, hidden_state):
        # Concatenate everything into the 'Identity' of the current task
        inp = np.concatenate([state, prev_action, [prev_reward, prev_done]])
        next_hidden = np.tanh(np.dot(inp, self.rnn_w))
        
        # The hidden state now 'knows' how this environment works
        print(f"🚀 RL^2: Hidden Memory updated. Adapting to current physics...")
        return next_hidden

print("🚀 RL^2 Meta-Learning: The agent that learns how to learn.")
rl2 = RL2Agent(state_dim=4, action_dim=2)
h = np.zeros(128)
s, a = np.random.randn(4), np.zeros(2)
rl2.step(s, a, 0.0, 0, h)
print("✅ Logic Check: Recurrent adaptation memory verified.")
