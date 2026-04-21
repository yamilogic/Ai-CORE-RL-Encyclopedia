import torch

def reward_model(output, preference):
    # Simulated Reward Model: Human preferred 'preference'
    return 1.0 if output == preference else -1.0

def rlhf_step(policy, query):
    outputs = ["Helpful Response", "Harmful Response"]
    selected = outputs[0] # Simulated policy choice
    reward = reward_model(selected, "Helpful Response")
    print(f"Query: {query} | Output: {selected} | Reward: {reward}")

print("🚀 RLHF Core: Aligning AI with Human Preferences.")
rlhf_step(None, "Write a poem")
print("✅ Feedback Loop: Reward model guides the policy update.")
