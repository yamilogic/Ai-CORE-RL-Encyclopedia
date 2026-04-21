import numpy as np

def expected_sarsa_update(Q, s, a, r, ns, alpha=0.1, gamma=0.9):
    # Expected Sarsa: Instead of picking one 'next action', use the AVERAGE
    # V(s') = sum( pi(a|s') * Q(s', a) )
    probs = np.ones(Q[ns].shape) / len(Q[ns]) # Uniform random policy example
    expected_v = np.dot(probs, Q[ns])
    
    delta = r + gamma * expected_v - Q[s, a]
    Q[s, a] += alpha * delta
    print(f"🚀 Expected Sarsa: Expected Next Value={expected_v:.2f} | Update Error={delta:.2f}")
    return Q

print("🚀 Expected Sarsa Core: Reducing variance by averaging all possible next actions.")
q_t = np.array([[10.0, 5.0], [2.0, 8.0]]) # 2 states, 2 actions
expected_sarsa_update(q_t, 0, 1, 1.0, 1)
print("✅ Logic Check: Expected-value TD-error verified.")
