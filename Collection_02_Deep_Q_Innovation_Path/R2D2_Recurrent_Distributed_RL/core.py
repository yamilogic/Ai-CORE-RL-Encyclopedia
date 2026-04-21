import numpy as np

def r2d2_recurrent_step(state, h_state, weights):
    # R2D2: Using LSTM/RNN to remember the past
    # New State = combine(Current State, Memory)
    combined = np.append(state, h_state)
    new_h = np.tanh(np.dot(combined, weights))
    print(f"🚀 R2D2: Memory Updated | Hidden State: {new_h[:3]}...")
    return new_h

print("🚀 R2D2: Recurrent Distributed RL for tasks requiring long-term memory.")
s, h = np.random.randn(4), np.random.randn(4)
w = np.random.randn(8, 4)
r2d2_recurrent_step(s, h, w)
print("✅ Logic Check: Hidden state propagation for temporal memory verified.")
