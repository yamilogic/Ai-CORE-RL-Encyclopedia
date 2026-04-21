import numpy as np

def ddpg_step(s, actor_w, critic_w):
    # Actor: Outputs a continuous action (e.g., Steering Angle)
    action = np.tanh(np.dot(s, actor_w)) 
    # Critic: Evaluates (State, Action) pair
    state_action = np.append(s, action)
    q_value = np.dot(state_action, critic_w)
    return action, q_value

print("🚀 DDPG Core: Continuous Control for Robotics and Driving.")
s = np.random.randn(3)
aw, cw = np.random.randn(3, 1), np.random.randn(4, 1)
a, q = ddpg_step(s, aw, cw)
print(f"✅ Action (Continuous): {a[0]:.4f} | Q-Value: {q[0]:.4f}")
print("Logic: The Actor learns to maximize the Critic's evaluation.")
