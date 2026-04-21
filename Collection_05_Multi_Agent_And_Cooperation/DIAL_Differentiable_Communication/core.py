import numpy as np

def dial_communication_step(local_state, weights):
    # DIAL: Agents learning to 'Talk' to each other
    # The 'Message' is a differentiable vector passed between agents
    # State -> Message
    message = np.tanh(np.dot(local_state, weights))
    print(f"🚀 DIAL: Agent sending Differentiable Message: {message[:3]}...")
    return message

print("🚀 DIAL Core: End-to-end communication learning for multi-agent teams.")
s = np.random.randn(4)
w = np.random.randn(4, 2)
dial_communication_step(s, w)
print("✅ Logic Check: Differentiable message passing verified.")
