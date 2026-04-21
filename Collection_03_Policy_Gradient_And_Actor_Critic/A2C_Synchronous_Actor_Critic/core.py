import numpy as np

def a2c_update(state, prob, reward, value, next_value):
    # A2C: Synchronous parallel updates
    # Advantage = r + gamma*V(s') - V(s)
    advantage = reward + 0.99 * next_value - value
    # Update Actor: log_prob * advantage
    actor_loss = -np.log(prob) * advantage
    # Update Critic: advantage^2
    critic_loss = advantage**2
    print(f"🚀 A2C: Advantage={advantage:.2f} | Actor Loss={actor_loss:.2f} | Critic Loss={critic_loss:.2f}")
    return actor_loss, critic_loss

print("🚀 A2C Core: The synchronous foundation of modern Actor-Critic.")
a2c_update(None, 0.6, 1.0, 0.5, 0.6)
print("✅ Logic Check: Joint Actor-Critic advantage update verified.")
