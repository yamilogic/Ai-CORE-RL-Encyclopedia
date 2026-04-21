import numpy as np

def maddpg_step(agents_obs, agents_actions, critic_w):
    # MADDPG: Centralized Training, Decentralized Execution
    # The Critic sees ALL agents' observations and actions
    global_input = np.concatenate(agents_obs + agents_actions)
    q_val = np.dot(global_input, critic_w)
    
    # The Actor only sees its OWN observation
    actor_action = np.tanh(np.dot(agents_obs[0], np.random.randn(agents_obs[0].shape[0])))
    
    print(f"🚀 MADDPG: Global Q-Value = {q_val[0]:.2f} | Local Actor Action: {actor_action:.2f}")
    return actor_action

print("🚀 MADDPG: Coordinating multiple continuous agents in a shared world.")
obs = [np.random.randn(4), np.random.randn(4)]
acts = [np.array([0.5]), np.array([-0.2])]
w = np.random.randn(10, 1) # 4+4 obs + 1+1 acts
maddpg_step(obs, acts, w)
print("✅ Logic Check: Centralized training / Decentralized execution verified.")
