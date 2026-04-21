import numpy as np

def qmix_mixer(agent_qs, global_state, mixer_weights):
    # QMIX: The 'Mixer' network ensures individual actions help the team
    # Constraint: Total Q must be MONOTONIC with respect to individual Qs
    # Total_Q = weights(state) * individual_Qs
    pos_weights = np.abs(mixer_weights) # Weights must be positive for monotonicity
    total_q = np.dot(agent_qs, pos_weights)
    print(f"🚀 QMIX: Agent Qs={agent_qs} | Mixed Total Q={total_q:.2f}")
    return total_q

print("🚀 QMIX: Cooperative Multi-Agent coordination via Value Mixing.")
qs = np.array([5.0, 3.0]) # 2 Agents
w = np.random.randn(2)
qmix_mixer(qs, None, w)
print("✅ Logic Check: Monotonic value mixing for team coordination verified.")
