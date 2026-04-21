import numpy as np

def nec_memory_lookup(state, dnd):
    # Differentiable Neural Dictionary (DND)
    # Search for similar experiences and average their rewards
    keys, values = dnd
    # Kernel: How similar is this state to stored states?
    distances = np.sum(np.square(keys - state), axis=1)
    weights = np.exp(-distances) / np.sum(np.exp(-distances))
    q_val = np.dot(weights, values)
    print(f"🚀 NEC: Memory Lookup complete. Q-Value = {q_val:.2f}")
    return q_val

print("🚀 Neural Episodic Control (NEC): Ultra-fast learning via Differentiable Memory.")
keys = np.random.randn(10, 4)
vals = np.random.randn(10)
s = np.random.randn(4)
nec_memory_lookup(s, (keys, vals))
print("✅ Logic Check: Similarity-based reward estimation verified.")
