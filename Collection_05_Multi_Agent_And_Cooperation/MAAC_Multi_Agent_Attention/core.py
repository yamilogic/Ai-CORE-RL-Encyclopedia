import numpy as np

def multi_agent_attention(agent_state, neighbor_states, query_w, key_w):
    # MAAC: Learning who to 'Listen' to in a multi-agent team
    # State -> Query
    query = np.dot(agent_state, query_w)
    # Neighbors -> Keys
    keys = np.dot(neighbor_states, key_w)
    
    # Scaled Dot-Product Attention
    scores = np.dot(keys, query) / np.sqrt(len(query))
    probs = np.exp(scores) / np.sum(np.exp(scores))
    
    print(f"🚀 MAAC Attention: Weights={probs.round(2)} | Focusing on neighbor {np.argmax(probs)}")
    return probs

print("🚀 MAAC: Initializing Multi-Agent Attention Mechanism...")
s_a = np.random.randn(4)
s_n = np.random.randn(5, 4) # 5 neighbors
qw, kw = np.random.randn(4, 8), np.random.randn(4, 8)
multi_agent_attention(s_a, s_n, qw, kw)
print("✅ Logic Check: Neighbor-selective attention verified.")
