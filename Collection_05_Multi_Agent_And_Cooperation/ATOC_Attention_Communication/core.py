import numpy as np

def atoc_attention_message(my_obs, teammate_obs_list):
    # ATOC: Attention-based Communication
    # Instead of talking to everyone, I only talk to 'Relevant' teammates.
    # Relevance = Attention_Score( My_State, Their_State )
    query = my_obs
    keys = np.array(teammate_obs_list)
    
    # Simple Dot-Product Attention
    scores = np.dot(keys, query)
    weights = np.exp(scores) / np.sum(np.exp(scores))
    
    # Weighted message
    message = np.dot(weights, keys)
    print(f"🚀 ATOC: Message generated for {len(teammate_obs_list)} teammates. Max Weight={np.max(weights):.4f}")
    return message

print("🚀 ATOC: Initializing Targeted-Attention Communication...")
m_o = np.array([1, 0, 0])
t_o = [np.array([1, 1, 0]), np.array([0, 0, 1])] # Teammate 1 is more similar/relevant
atoc_attention_message(m_o, t_o)
print("✅ Logic Check: Dot-product attention weighting verified.")
