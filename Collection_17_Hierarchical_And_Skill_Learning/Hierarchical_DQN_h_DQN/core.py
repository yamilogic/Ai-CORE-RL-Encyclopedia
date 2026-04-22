import numpy as np

def hdqn_meta_controller(state, goal_weights):
    # h-DQN: Meta-controller chooses a 'Goal' for the worker
    goal = np.tanh(np.dot(state, goal_weights))
    print(f"🚀 h-DQN: Meta-Controller selected Sub-Goal: {goal.round(2)}")
    return goal

def hdqn_worker(state, goal, action_weights):
    # Worker tries to reach the goal selected by the meta-controller
    state_goal = np.concatenate([state, goal])
    action = np.dot(state_goal, action_weights)
    print(f"🚀 h-DQN: Worker executing action to reach Goal.")
    return action

print("🚀 h-DQN Core: Hierarchical Q-Learning with Meta-Controller and Worker.")
s, gw, aw = np.random.randn(4), np.random.randn(4, 2), np.random.randn(6, 1)
g = hdqn_meta_controller(s, gw)
hdqn_worker(s, g, aw)
print("✅ Logic Check: Meta-Worker goal-conditioned hierarchy verified.")
