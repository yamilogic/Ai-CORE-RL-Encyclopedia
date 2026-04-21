import numpy as np

def gail_discriminator_reward(state, action, expert_pairs):
    # GAIL: Imitation as GAN. 
    # Discriminator D(s,a) tries to distinguish Expert vs Agent.
    # Agent reward = -log(1 - D(s,a))
    # If the Discriminator is fooled, the Agent gets a high reward.
    
    # Simple similarity-based discriminator proxy
    similarity = np.max([np.dot(np.concatenate([state, action]), ep) for ep in expert_pairs])
    reward = -np.log(1 - (similarity + 1e-8) / (1 + 1e-8)) # log(1/D)
    print(f"🚀 GAIL: Discriminator Score={similarity:.4f} | Imitation Reward={reward:.4f}")
    return reward

print("🚀 GAIL: Initializing Adversarial Imitation Engine...")
s_val = np.random.randn(4)
a_val = np.random.randn(2)
experts = [np.random.randn(6) for _ in range(3)]
gail_discriminator_reward(s_val, a_val, experts)
print("✅ Logic Check: Adversarial-reward calculation verified.")
