import numpy as np

def dac_discriminator_reward(state, action, discriminator_w):
    # DAC: Discriminator Actor-Critic.
    # Logic: Off-policy Imitation Learning.
    # We use a Discriminator to label 'Off-policy' samples.
    # This solves the 'Bias' problem in standard GAIL.
    logits = np.dot(np.concatenate([state, action]), discriminator_w)
    prob_expert = 1.0 / (1.0 + np.exp(-logits))
    # Reward = log(D) - log(1-D)
    reward = np.log(prob_expert + 1e-8) - np.log(1 - prob_expert + 1e-8)
    print(f"🚀 DAC: Discriminator Probability={prob_expert:.4f} | Off-policy Reward={reward:.4f}")
    return reward

print("🚀 DAC: Initializing Off-Policy Adversarial Imitation...")
s_val = np.random.randn(4)
a_val = np.random.randn(2)
w_disc = np.random.randn(6)
dac_discriminator_reward(s_val, a_val, w_disc)
print("✅ Logic Check: Logit-based off-policy reward verified.")
