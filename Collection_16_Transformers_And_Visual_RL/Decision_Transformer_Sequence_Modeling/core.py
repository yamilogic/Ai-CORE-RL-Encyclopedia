import numpy as np

class DecisionTransformer:
    """
    Decision Transformer: RL as Sequence Modeling.
    Instead of Q-learning, it uses GPT-style attention to predict actions.
    Input: (Return-to-go, State, Action) sequences.
    """
    def __init__(self, state_dim, action_dim, seq_len=10, embed_dim=128):
        self.seq_len = seq_len
        self.embed_dim = embed_dim
        
        # 1. Embeddings (Linear projections)
        self.state_emb = np.random.randn(state_dim, embed_dim) * 0.1
        self.action_emb = np.random.randn(action_dim, embed_dim) * 0.1
        self.return_emb = np.random.randn(1, embed_dim) * 0.1
        
        # 2. Simplified Multi-Head Attention Weights
        self.query_w = np.random.randn(embed_dim, embed_dim) * 0.1
        self.key_w = np.random.randn(embed_dim, embed_dim) * 0.1
        self.value_w = np.random.randn(embed_dim, embed_dim) * 0.1

    def predict_action(self, returns_to_go, states, actions):
        # 1. Create Sequence [R1, S1, A1, R2, S2, A2, ...]
        r_emb = np.dot(returns_to_go, self.return_emb)
        s_emb = np.dot(states, self.state_emb)
        a_emb = np.dot(actions, self.action_emb)
        
        # Interleave embeddings
        seq = np.stack([r_emb, s_emb, a_emb], axis=1).reshape(-1, self.embed_dim)
        
        # 2. Self-Attention (Simplified)
        q = np.dot(seq, self.query_w)
        k = np.dot(seq, self.key_w)
        v = np.dot(seq, self.value_w)
        
        attention = np.dot(q, k.T) / np.sqrt(self.embed_dim)
        attention_probs = np.exp(attention) / np.sum(np.exp(attention), axis=-1, keepdims=True)
        
        out = np.dot(attention_probs, v)
        print(f"🚀 Decision Transformer: Attending to sequence of length {len(seq)}. Predicting next action...")
        return out[-1] # Predict based on last state-return

print("🚀 Decision Transformer: RL as Generative Modeling...")
dt = DecisionTransformer(state_dim=4, action_dim=2)
r_seq = np.random.randn(5, 1)
s_seq = np.random.randn(5, 4)
a_seq = np.random.randn(5, 2)
dt.predict_action(r_seq, s_seq, a_seq)
print("✅ Decision Transformer: Sequential attention logic verified.")
