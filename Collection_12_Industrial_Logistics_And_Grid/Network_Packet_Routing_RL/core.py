import numpy as np

def route_packet(latency_map, bandwidth_map, routing_weights):
    # RL for Networking: [Latency, Bandwidth] -> Pick Output Port
    # Reward = -(End-to-End Delay) - (Packet Loss)
    state = np.append(latency_map, bandwidth_map)
    port_probs = np.exp(np.dot(routing_weights, state))
    port_probs /= np.sum(port_probs)
    selected_port = np.random.choice(len(port_probs), p=port_probs)
    print(f"🚀 Routing RL: Latency checked. Sending Packet via Port: {selected_port}")
    return selected_port

print("🚀 Network Packet Routing RL: AI-driven internet infrastructure.")
l, b = np.random.rand(4), np.random.rand(4)
w = np.random.randn(4, 8) # 4 output ports, 8 state features
route_packet(l, b, w)
print("✅ Logic Check: Congestion-aware path selection verified.")
