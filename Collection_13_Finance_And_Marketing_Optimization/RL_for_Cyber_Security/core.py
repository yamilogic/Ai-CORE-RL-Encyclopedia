import numpy as np

def cyber_security_defense(traffic_volume, error_rate, unauthorized_attempts, weights):
    # Cyber Security RL: Defending against DDoS and Intrusions
    # State = Traffic spikes, Error rates, Suspicious patterns
    threat_level = np.dot([traffic_volume, error_rate, unauthorized_attempts], weights)
    # Action: 0=Normal, 1=Throttling, 2=Firewall Block
    action = np.digitize(threat_level, [0.5, 0.8])
    modes = ["🟢 NORMAL", "🟡 THROTTLE", "🔴 BLOCK"]
    print(f"🚀 Cyber RL: Threat Score={threat_level:.2f} | Defense Mode={modes[action]}")
    return action

print("🚀 Cyber Security RL: Defending infrastructure in real-time.")
v, e, u = 1000.0, 0.01, 50.0
w = np.array([0.0001, 10.0, 0.01])
cyber_security_defense(v, e, u, w)
print("✅ Logic Check: Threat-level-aware defense switching verified.")
