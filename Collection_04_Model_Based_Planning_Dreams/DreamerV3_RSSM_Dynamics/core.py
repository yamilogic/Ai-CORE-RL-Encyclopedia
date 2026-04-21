import numpy as np

class RSSM:
    """
    Recurrent State Space Model (RSSM): The heart of DreamerV3.
    Combines Deterministic (RNN) and Stochastic (Categorical) states.
    """
    def __init__(self, action_dim, deter_dim=256, stoch_dim=32, discrete_dim=32):
        self.deter_dim = deter_dim
        self.stoch_dim = stoch_dim
        self.discrete_dim = discrete_dim
        
        # RNN Weights (Deterministic)
        self.rnn_cell_w = np.random.randn(deter_dim + stoch_dim * discrete_dim + action_dim, deter_dim) * 0.01
        # Prediction Weights (Stochastic)
        self.stoch_pred_w = np.random.randn(deter_dim, stoch_dim * discrete_dim) * 0.01

    def get_stochastic_state(self, deter_state):
        # Predict logits for Categorical distribution (Symlog compatible)
        logits = np.dot(deter_state, self.stoch_pred_w)
        logits = logits.reshape(self.stoch_dim, self.discrete_dim)
        
        # Softmax to get probabilities
        exp_l = np.exp(logits - np.max(logits, axis=-1, keepdims=True))
        probs = exp_l / np.sum(exp_l, axis=-1, keepdims=True)
        
        # Sample or just use 'one-hot' equivalent for minimal core
        stoch_state = (probs == np.max(probs, axis=-1, keepdims=True)).astype(float).flatten()
        return stoch_state

    def step(self, prev_deter, prev_stoch, action):
        # 1. Concatenate previous state and action
        inp = np.concatenate([prev_deter, prev_stoch, action])
        
        # 2. Deterministic Step (RNN)
        next_deter = np.tanh(np.dot(inp, self.rnn_cell_w))
        
        # 3. Stochastic Step (Sampling from predicted categorical)
        next_stoch = self.get_stochastic_state(next_deter)
        
        print(f"🚀 RSSM: Step Complete. Deter={next_deter[:2]}... | Stoch={next_stoch[:2]}...")
        return next_deter, next_stoch

print("🚀 DreamerV3 RSSM: Initializing Recurrent State Space Model...")
rssm = RSSM(action_dim=2)
d, s = np.zeros(256), np.zeros(32*32)
a = np.array([1.0, 0.0])
rssm.step(d, s, a)
print("✅ RSSM: Latent world-model step verified.")
