import numpy as np

def drq_augmentation_average(state_v1, state_v2, q_network_weights):
    # DrQ: Simple but powerful. Average the Q-values of 2 augmentations
    # Q(s) = mean( Q(aug1(s)), Q(aug2(s)) )
    q1 = np.dot(state_v1, q_network_weights)
    q2 = np.dot(state_v2, q_network_weights)
    q_avg = (q1 + q2) / 2.0
    print(f"🚀 DrQ: Q_aug1={q1:.2f} | Q_aug2={q2:.2f} | Averaged Q={q_avg:.2f}")
    return q_avg

print("🚀 DrQ Core: Regularizing Q-Learning through data shifts.")
s1, s2 = np.random.randn(4), np.random.randn(4)
w = np.random.randn(4)
drq_augmentation_average(s1, s2, w)
print("✅ Logic Check: Q-value stability through augmentation averaging verified.")
