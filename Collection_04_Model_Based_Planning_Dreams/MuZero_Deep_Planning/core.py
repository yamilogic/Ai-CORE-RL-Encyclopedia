import numpy as np

class MuZeroLatentDynamics:
    """
    MuZero: Planning within a learned world model.
    Learns 3 Networks: Representation (h), Dynamics (g), and Prediction (f).
    """
    def __init__(self, state_dim, latent_dim, action_dim):
        # 1. Representation (s -> s_latent)
        self.repr_weights = np.random.randn(state_dim, latent_dim) * 0.1
        # 2. Dynamics (s_latent, a -> s_next_latent, reward)
        self.dyn_weights = np.random.randn(latent_dim + action_dim, latent_dim + 1) * 0.1
        # 3. Prediction (s_latent -> policy_probs, value)
        self.pred_weights = np.random.randn(latent_dim, action_dim + 1) * 0.1

    def initial_inference(self, state):
        # h(s) -> s_latent
        s_latent = np.tanh(np.dot(state, self.repr_weights))
        return s_latent, self.predict(s_latent)

    def recurrent_inference(self, s_latent, action):
        # g(s_latent, a) -> s_next_latent, r
        action_vec = np.zeros(self.pred_weights.shape[0]-3) # placeholder
        inp = np.concatenate([s_latent, [action]])
        out = np.tanh(np.dot(inp, self.dyn_weights))
        s_next_latent, reward = out[:-1], out[-1]
        return s_next_latent, reward, self.predict(s_next_latent)

    def predict(self, s_latent):
        # f(s_latent) -> pi, v
        out = np.dot(s_latent, self.pred_weights)
        pi_logits, v = out[:-1], out[-1]
        pi_probs = np.exp(pi_logits) / np.sum(np.exp(pi_logits))
        return pi_probs, v

    def plan_with_mcts(self, state, depth=5):
        # Simple MCTS-style planning within the latent model
        s_latent, (pi, v) = self.initial_inference(state)
        total_v = v
        
        current_s = s_latent
        for _ in range(depth):
            best_a = np.argmax(pi)
            current_s, r, (pi, v) = self.recurrent_inference(current_s, best_a)
            total_v += r + v
            
        print(f"🚀 MuZero: Planned {depth} steps in latent space. Total Est Value: {total_v:.2f}")
        return np.argmax(pi)

print("🚀 MuZero: Initializing Learned Planning Architecture...")
mu = MuZeroLatentDynamics(state_dim=8, latent_dim=16, action_dim=4)
obs = np.random.randn(8)
mu.plan_with_mcts(obs)
print("✅ MuZero: Planning inside the mind of the agent complete.")
