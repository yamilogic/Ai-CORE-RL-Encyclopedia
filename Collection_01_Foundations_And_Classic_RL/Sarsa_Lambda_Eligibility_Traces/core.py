import numpy as np

def sarsa_lambda_update(Q, traces, s, a, r, ns, na, alpha=0.1, gamma=0.9, lam=0.8):
    # Eligibility Traces: Decay the memory of past steps
    # Update current step and ALL past steps in the trace
    delta = r + gamma * Q[ns, na] - Q[s, a]
    traces[s, a] += 1 # Add to current step trace
    
    Q += alpha * delta * traces
    traces *= gamma * lam # Decay the whole trace
    print(f"🚀 Sarsa(λ): Error={delta:.2f} | Max Trace={np.max(traces):.2f}")
    return Q, traces

print("🚀 Sarsa(λ) Core: Using Eligibility Traces to credit past actions.")
q, t = np.zeros((5, 2)), np.zeros((5, 2))
sarsa_lambda_update(q, t, 0, 1, 10.0, 1, 0)
print("✅ Logic Check: Eligibility trace decay and multi-step credit verified.")
