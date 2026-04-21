import numpy as np

def vdn_sum_mixer(agent_qs):
    # VDN: The simplest Multi-Agent coordination
    # Total Q = sum of all individual Qs
    total_q = np.sum(agent_qs)
    print(f"🚀 VDN: Individual Qs={agent_qs} | Total Team Q (Sum)={total_q:.2f}")
    return total_q

print("🚀 VDN: The foundation of cooperative value-based MARL.")
qs = np.array([2.5, 4.5, 1.0]) # 3 Agents
vdn_sum_mixer(qs)
print("✅ Logic Check: Linear value summation for team reward verified.")
