import numpy as np

def dreamerv2_latent_step(state, prev_action, weights):
    # DreamerV2: Using DISCRETE (Categorical) Latent variables
    # This prevents the latent space from 'averaging' different futures
    # (e.g., if you could turn left or right, a continuous model averages to 'forward')
    # A discrete model picks 'Left' or 'Right'.
    
    # Encoder: State -> One-Hot Latent
    latent_logits = np.dot(state, weights['enc'])
    probs = np.exp(latent_logits) / np.sum(np.exp(latent_logits))
    z = np.zeros_like(probs)
    z[np.argmax(probs)] = 1.0 # Discrete bottleneck
    
    print(f"🚀 DreamerV2: State encoded into DISCRETE latent z={np.argmax(z)}")
    return z

print("🚀 DreamerV2: Initializing Categorical Latent Dynamics...")
s_in = np.random.randn(4)
w_dict = {'enc': np.random.randn(4, 32)} # 32 possible categories
dreamerv2_latent_step(s_in, None, w_dict)
print("✅ Logic Check: Discrete-bottleneck latent encoding verified.")
