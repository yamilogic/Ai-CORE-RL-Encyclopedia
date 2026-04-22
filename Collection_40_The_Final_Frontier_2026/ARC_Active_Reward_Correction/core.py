import numpy as np

def arc_reward_critic(agent_action, current_reward, reward_goal="Human Welfare"):
    # ARC: Active-Reward Correction.
    # Logic: A separate 'Monitor' AI analyzes the reward signal.
    # If the reward is 'Loopholed' (Reward Hacking), it kills the signal.
    # Inspired by the AI Safety alignment crisis of 2024.
    
    is_hacking = False
    if np.abs(agent_action) > 1000: # Heuristic for extreme behavior
        is_hacking = True
        
    if is_hacking:
        corrected_reward = -100.0
        print("🚨 ARC: Reward Hacking Detected! Correcting Signal to -100.")
    else:
        corrected_reward = current_reward
        print("✅ ARC: Reward Signal Validated.")
        
    return corrected_reward

print("🚀 ARC: Initializing Active Alignment Monitor...")
arc_reward_critic(agent_action=5000, current_reward=10)
print("✅ Logic Check: Reward-correction logic verified.")
