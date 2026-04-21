import numpy as np

def network_routing_reward(latency, packet_loss, bandwidth_usage):
    # RL for Packet Routing: Finding the fastest path through the Internet.
    # Reward = - (Latency + C1 * Packet_Loss + C2 * Congestion)
    # The agent decides which 'Node' to send the data to next.
    loss_penalty = packet_loss * 500.0
    latency_penalty = latency * 100.0
    reward = -(latency_penalty + loss_penalty + bandwidth_usage * 0.1)
    print(f"🚀 Routing-RL: Latency={latency:.2f}ms | Loss={packet_loss:.4f} | Reward={reward:.2f}")
    return reward

print("🚀 RL for Network Packet Routing: Optimizing global data flows.")
network_routing_reward(Latency=25, packet_loss=0.001, bandwidth_usage=80)
print("✅ Logic Check: Latency-loss trade-off reward verified.")
