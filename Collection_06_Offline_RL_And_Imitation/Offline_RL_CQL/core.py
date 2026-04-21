import numpy as np

def conservative_q_update(dataset, Q):
    # dataset = [(s, a, r)]
    for s, a, r in dataset:
        # Standard update
        Q[s, a] += 0.1 * (r - Q[s, a])
        # Conservative Penalty: Push down Q-values of actions NOT in dataset
        # This prevents overestimation of unseen actions
        Q[s, 1-a] -= 0.05 
    return Q

print("🚀 Offline RL (CQL): Learning from History without an Environment.")
Q = np.zeros((2, 2))
data = [(0, 1, 10), (1, 0, 5)] # (State, Action, Reward)
Q = conservative_q_update(data, Q)
print(f"✅ Learned Q-Table: \n{Q}")
print("Logic: Higher values for data we have, penalty for data we don't.")
