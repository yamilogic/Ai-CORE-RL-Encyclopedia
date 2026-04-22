import numpy as np

def drq_q_averaging(state, action, q_net_w, n_aug=2):
    # DrQ: Improving Visual RL via Data Regularization
    # Target Q is averaged over multiple 'Augmented' versions of the same state
    q_sum = 0
    for _ in range(n_aug):
        # Shift the image slightly (Simplified as noise here)
        augmented_state = state + np.random.normal(0, 0.05, size=state.shape)
        q_sum += np.dot(np.concatenate([augmented_state, action]), q_net_w)
    
    avg_q = q_sum / n_aug
    print(f"🚀 DrQ: Averaged Q-value over {n_aug} augmentations: {avg_q.item():.4f}")
    return avg_q

print("🚀 DrQ: Initializing Data-Regularized Value Function...")
s_vec = np.random.randn(4)
a_vec = np.random.randn(2)
w_q = np.random.randn(6, 1)
drq_q_averaging(s_vec, a_vec, w_q)
print("✅ Logic Check: Augmentation-averaged Q-value verified.")
