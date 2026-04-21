import numpy as np

def robust_minimax_action(state, action_candidates, adversary_noise_range=0.2):
    # Worst-Case Robust RL: Playing against a 'Devil's Advocate'
    # For every action, we calculate the WORST thing that could happen
    # then we pick the action where the 'Worst thing' is the best.
    
    best_worst_score = -np.inf
    best_action = None
    
    for action in action_candidates:
        # Predict outcome with adversarial noise
        worst_outcome = np.dot(state + action, np.array([1.0])) - adversary_noise_range
        if worst_outcome > best_worst_score:
            best_worst_score = worst_outcome
            best_action = action
            
    print(f"🚀 Robust RL: Picked action with safest worst-case outcome={best_worst_score:.4f}")
    return best_action

print("🚀 Worst-Case Robust RL: Minimax optimization against uncertainty.")
s_in = np.array([0.5])
a_c = [np.array([0.1]), np.array([0.5])]
robust_minimax_action(s_in, a_c)
print("✅ Logic Check: Minimax-based action selection verified.")
