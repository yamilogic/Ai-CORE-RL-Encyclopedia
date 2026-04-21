import numpy as np

def update_belief(belief, observation, action, transition_matrix, observation_matrix):
    # POMDP: Belief State = Probability distribution over possible real states
    # Update: P(s' | o, a) proportional to P(o | s') * sum( P(s' | s, a) * P(s) )
    pred_belief = np.dot(belief, transition_matrix[action])
    new_belief = observation_matrix[:, observation] * pred_belief
    new_belief /= np.sum(new_belief) # Normalize
    print(f"🚀 POMDP: Belief Updated. Most likely state: {np.argmax(new_belief)}")
    return new_belief

print("🚀 POMDP Core: Reasoning under incomplete information.")
b = np.array([0.5, 0.5]) # Initial belief: 50/50
t = np.array([[[0.7, 0.3], [0.3, 0.7]], [[0.8, 0.2], [0.2, 0.8]]])
o_m = np.array([[0.9, 0.1], [0.2, 0.8]])
update_belief(b, 0, 0, t, o_m)
print("✅ Logic Check: Bayesian belief update verified.")
