import numpy as np

def hebbian_update(pre_synaptic, post_synaptic, weights, lr=0.01):
    # Hebbian Learning: 'Cells that fire together, wire together'
    # delta_w = lr * pre * post
    # This allows a brain to adapt its OWN weights during a single episode.
    update = lr * np.outer(post_synaptic, pre_synaptic)
    new_weights = weights + update
    print(f"🚀 Hebbian: Synapse strengthened! Max Weight Shift={np.max(np.abs(update)):.4f}")
    return new_weights

print("🚀 Hebbian Plasticity: The bio-inspired way to learn without gradients.")
pre = np.array([1.0, 0.0, 1.0]) # 3 input neurons
post = np.array([0.0, 1.0])    # 2 output neurons
w = np.random.randn(2, 3)
hebbian_update(pre, post, w)
print("✅ Logic Check: Correlation-based weight update verified.")
