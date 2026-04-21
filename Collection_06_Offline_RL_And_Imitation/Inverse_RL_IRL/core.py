import numpy as np

def expert_demo(): return [0, 1, 2, 3, 4] # Expert always moves right

def train_irl():
    learned_rewards = np.zeros(5)
    expert_path = expert_demo()
    for _ in range(50):
        # Update rewards so expert's path has higher values
        for s in expert_path: learned_rewards[s] += 0.1
        learned_rewards -= 0.05 # Decay others
    return learned_rewards

print("🚀 Inverse RL: Learning the Reward Function from Experts.")
rewards = train_irl()
print(f"✅ Learned Rewards: {rewards.round(1)}")
print(f"Logic: Higher rewards found at states {np.where(rewards > 0.5)[0]} (Expert Path)")
