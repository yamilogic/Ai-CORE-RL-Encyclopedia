import numpy as np

def expected_sarsa_update(Q, s, a, r, ns, alpha=0.1, gamma=0.9):
    # Instead of max(Q[ns]), use the EXPECTED value based on policy
    # (Assuming uniform random policy for this demo)
    expected_v = np.mean(Q[ns])
    Q[s, a] += alpha * (r + gamma * expected_v - Q[s, a])
    return Q

print("🚀 Expected Sarsa: Stable learning through probabilistic expectations.")
Q = np.zeros((5, 2))
expected_sarsa_update(Q, 0, 1, 10.0, 1)
print(f"✅ Q-Value Updated: {Q[0, 1]:.2f} | Using average of next state values.")
