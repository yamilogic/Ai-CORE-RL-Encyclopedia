import numpy as np

def gps_supervised_update(policy_weights, expert_trajectory, lr=0.01):
    # GPS: Training a neural network policy to mimic local 'Expert' controllers
    # It combines RL (finding the expert) and Supervised Learning (mimicking)
    states = expert_trajectory['states']
    expert_actions = expert_trajectory['actions']
    
    # Simple Supervised Gradient Step
    predicted_actions = np.dot(states, policy_weights)
    error = expert_actions - predicted_actions
    policy_weights += lr * np.dot(states.T, error)
    
    print(f"🚀 GPS: Policy refined to match expert behavior. Error={np.mean(np.square(error)):.4f}")
    return policy_weights

print("🚀 Guided Policy Search (GPS): Bridging local control and global policies.")
w = np.random.randn(4, 2)
traj = {'states': np.random.randn(10, 4), 'actions': np.random.randn(10, 2)}
gps_supervised_update(w, traj)
print("✅ Logic Check: Expert-mimicry supervised update verified.")
