import numpy as np

def dreamer_latent_step(state, action, model_w):
    # RSSM (Recurrent State-Space Model) logic
    # Instead of predicting pixels, we predict 'Latent States' (compact thoughts)
    latent_s = np.tanh(np.dot(np.append(state, action), model_w))
    reward_pred = np.dot(latent_s, np.random.randn(latent_s.shape[0]))
    return latent_s, reward_pred

print("🚀 Dreamer Core: Planning and Training inside a Latent World Model.")
s, a = np.random.randn(10), 1
w = np.random.randn(11, 10)
ls, rp = dreamer_latent_step(s, a, w)
print(f"✅ Latent Thought: {ls[:3]}... | Predicted Reward: {rp:.2f}")
print("Logic: The agent 'thinks' in a compressed space to simulate millions of steps.")
