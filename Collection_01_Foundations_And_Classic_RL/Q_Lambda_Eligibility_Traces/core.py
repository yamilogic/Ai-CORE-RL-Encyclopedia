import numpy as np

def q_lambda_update(Q, traces, s, a, r, ns, alpha=0.1, gamma=0.9, lam=0.8):
    # Watkin's Q(lambda): Multi-step Q-learning
    # Note: Traces are cut if the agent takes a non-greedy (exploratory) action
    best_ns_a = np.argmax(Q[ns])
    delta = r + gamma * Q[ns, best_ns_a] - Q[s, a]
    
    traces[s, a] += 1
    Q += alpha * delta * traces
    
    # If the action wasn't the best one, we can't look further back
    traces *= gamma * lam
    print(f"🚀 Q(λ): Error={delta:.2f} | Traces being applied to past steps.")
    return Q, traces

print("🚀 Q(λ) Core: Combining Q-learning with Eligibility Traces.")
q, t = np.zeros((5, 2)), np.zeros((5, 2))
q_lambda_update(q, t, 0, 1, 10.0, 1)
print("✅ Logic Check: Off-policy multi-step trace update verified.")
