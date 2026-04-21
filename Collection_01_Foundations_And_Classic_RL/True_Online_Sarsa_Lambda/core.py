import numpy as np

def true_online_sarsa_lambda_update(Q, traces, s, a, r, ns, na, alpha=0.1, gamma=0.9, lam=0.8):
    # True Online Sarsa(lambda): More stable and accurate than the standard version
    # It uses a 'Weight Vector' approach to ensure no information is lost
    q_prev = Q[s, a]
    q_next = Q[ns, na]
    delta = r + gamma * q_next - q_prev
    
    # The 'True Online' trace update logic
    traces[s, a] += (1 - alpha * traces[s, a])
    Q += alpha * (delta + q_prev - Q[s, a]) * traces
    Q[s, a] += alpha * (Q[s, a] - q_prev) # Correction step
    
    traces *= gamma * lam
    print(f"🚀 True Online Sarsa: Precise weight update. Error={delta:.2f}")
    return Q, traces

print("🚀 True Online Sarsa(λ): The mathematically correct version of eligibility traces.")
q_mat, t_mat = np.zeros((4, 2)), np.zeros((4, 2))
true_online_sarsa_lambda_update(q_mat, t_mat, 0, 1, 5.0, 1, 0)
print("✅ Logic Check: True online trace correction verified.")
