import numpy as np

def dueling_predict(s, w_v, w_a):
    # State Value (V): How good is this state?
    v = np.dot(s, w_v)
    # Advantage (A): How much better is each action?
    a = np.dot(s, w_a)
    # Combine: Q = V + (A - mean(A))
    q = v + (a - np.mean(a))
    return q

print("🚀 Dueling DQN Core: Separating 'State Value' from 'Action Advantage'.")
s = np.random.randn(4)
wv, wa = np.random.randn(4, 1), np.random.randn(4, 3)
q_values = dueling_predict(s, wv, wa)
print(f"✅ Q-Values for 3 actions: {q_values.flatten()}")
print("Logic: The network learns which states are good, regardless of actions.")
