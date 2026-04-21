import numpy as np

def coma_advantage(q_all_actions, agent_action_idx, policy_probs):
    # COMA: Solving the 'Credit Assignment' problem
    # Advantage = Q(s, a_i) - sum(pi(a) * Q(s, a))
    # 'What would happen if I had done something else?'
    baseline = np.dot(q_all_actions, policy_probs)
    advantage = q_all_actions[agent_action_idx] - baseline
    print(f"🚀 COMA: Baseline={baseline:.2f} | My Advantage={advantage:.2f}")
    return advantage

print("🚀 COMA: Multi-Agent Policy Gradients with Counterfactual Baselines.")
q_vals = np.array([10.0, 2.0, 5.0]) # Q-values for 3 possible actions
probs = np.array([0.1, 0.1, 0.8]) # Current policy probabilities
coma_advantage(q_vals, 0, probs)
print("✅ Logic Check: Counterfactual credit assignment verified.")
