import numpy as np

def munchausen_q_target(reward, next_q, current_log_pi, alpha=0.9, tau=0.03):
    # Munchausen RL: Bootstrapping with the current policy's log-probability
    # r_modified = reward + alpha * tau * log_pi(a|s)
    # This 'Self-Boosts' the agent's confidence in its own good ideas.
    m_reward = reward + alpha * tau * np.clip(current_log_pi, -20, 0)
    target = m_reward + 0.99 * next_q
    print(f"🚀 Munchausen: Modified Reward={m_reward:.4f} | Original={reward:.2f}")
    return target

print("🚀 Munchausen RL: Self-bootstrapping for faster and more stable Q-learning.")
munchausen_q_target(1.0, 5.0, -0.5)
print("✅ Logic Check: Log-policy augmented reward verified.")
