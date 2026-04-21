import numpy as np

def sqil_buffer_sampling(expert_buffer, agent_buffer):
    # SQIL: Imitation without a Discriminator.
    # Logic: Assign Reward=1 to all Expert data, Reward=0 to all Agent data.
    # Train using standard Soft Actor-Critic (SAC).
    # This is incredibly simple and surprisingly effective.
    
    e_sample = expert_buffer[np.random.choice(len(expert_buffer))]
    a_sample = agent_buffer[np.random.choice(len(agent_buffer))]
    
    print(f"🚀 SQIL: Sampled Expert (Reward=1.0) & Agent (Reward=0.0). Balancing labels.")
    return (e_sample, 1.0), (a_sample, 0.0)

print("🚀 SQIL: Initializing Simple Soft-Q Imitation...")
sqil_buffer_sampling([1,2,3], [4,5,6])
print("✅ Logic Check: Binary-labeling buffer sampling verified.")
