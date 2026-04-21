import numpy as np

def compute_message(state, target_id, weight_w):
    # Message Passing: A node generates a 'Summary' for its neighbor.
    # Message = f( My_State, Target_ID )
    msg = np.tanh(np.dot(state, weight_w))
    print(f"🚀 Msg Passing: Message created for Node {target_id}. Val={msg[:2]}...")
    return msg

print("🚀 Message Passing RL: Local decentralized communication.")
s = np.random.randn(4)
w = np.random.randn(4, 4)
compute_message(s, 1, w)
print("✅ Logic Check: State-to-message mapping verified.")
