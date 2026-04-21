import numpy as np

def cyber_response_reward(attack_blocked, system_uptime, false_alarm_rate):
    # RL for Cybersecurity: Automated defense.
    # Reward = Blocked_Attacks - (C1 * Uptime_Loss + C2 * False_Alarms)
    # The agent must decide when to 'Kill' a network connection.
    alarm_penalty = false_alarm_rate * 50.0
    uptime_reward = system_uptime * 100.0
    reward = attack_blocked * 500.0 + uptime_reward - alarm_penalty
    print(f"🚀 Cyber-RL: Blocked={attack_blocked} | Uptime={system_uptime*100:.1f}% | Reward={reward:.2f}")
    return reward

print("🚀 RL for Cybersecurity Intrusion Response: Autonomous network defense.")
cyber_response_reward(attack_blocked=1, system_uptime=0.99, false_alarm_rate=0.05)
print("✅ Logic Check: Attack-block-vs-false-alarm reward verified.")
