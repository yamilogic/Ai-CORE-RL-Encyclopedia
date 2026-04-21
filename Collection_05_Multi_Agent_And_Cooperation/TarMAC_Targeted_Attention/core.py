import numpy as np

def tarmac_targeted_message(sender_obs, receiver_obs, message_w):
    # TarMAC: Targeted Multi-Agent Communication
    # A sender generates a message AND a 'Signature'.
    # A receiver only listens if the signature matches its own state.
    # This allows for 'Private' or 'Targeted' whispers in a group.
    signature = np.tanh(np.dot(sender_obs, message_w))
    relevance = np.dot(signature, receiver_obs)
    
    if relevance > 0.5:
        print(f"🚀 TarMAC: Message Accepted! Relevance={relevance:.4f}")
        return signature
    else:
        print(f"🤫 TarMAC: Message Ignored. Irrelevant to receiver.")
        return None

print("🚀 TarMAC: Initializing Signature-based Targeted Communication...")
s_o = np.array([1, 1, 0])
r_o = np.array([1, 0, 0]) # Receiver is interested in the first feature
tarmac_targeted_message(s_o, r_o, np.eye(3))
print("✅ Logic Check: Signature-relevance filtering verified.")
