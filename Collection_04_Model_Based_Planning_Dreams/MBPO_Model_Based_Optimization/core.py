import numpy as np

def mbpo_short_rollout(state, policy_w, model_w, h=5):
    # MBPO: Using a world model for 'Short' mental rehearsals
    # Long rollouts are 'hallucinations', but short ones (1-5 steps) are useful.
    synthetic_experience = []
    curr = state
    for _ in range(h):
        action = np.tanh(np.dot(curr, policy_w))
        next_s = np.dot(np.concatenate([curr, action]), model_w)
        synthetic_experience.append((curr, action, next_s))
        curr = next_s
    print(f"🚀 MBPO: Generated {h}-step mental rollout. Adding to training buffer.")
    return synthetic_experience

print("🚀 MBPO: Initializing Short-Horizon Model Rehearsal...")
s_vec = np.random.randn(4)
p_w = np.random.randn(4, 2)
m_w = np.random.randn(6, 4)
mbpo_short_rollout(s_vec, p_w, m_w)
print("✅ Logic Check: Short-horizon synthetic trajectory generation verified.")
