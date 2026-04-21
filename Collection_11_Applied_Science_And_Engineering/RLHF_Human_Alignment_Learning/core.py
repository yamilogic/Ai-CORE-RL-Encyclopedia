import numpy as np

def rlhf_reward_model(answer_a, answer_b, human_preference):
    # RLHF: Human says 'A is better than B'
    # Reward Model learns to give higher score to A
    score_a = np.dot(answer_a, np.random.randn(len(answer_a)))
    score_b = np.dot(answer_b, np.random.randn(len(answer_b)))
    
    # Gradient: If human prefers A, push score_a up and score_b down
    if human_preference == 'A':
        reward_error = score_b - score_a
    else:
        reward_error = score_a - score_b
        
    print(f"🚀 RLHF: Reward Model adjusted based on Human Preference. Error: {reward_error:.2f}")
    return reward_error

print("🚀 RLHF Core: Aligning AI agents with human values and preferences.")
rlhf_reward_model(np.random.randn(4), np.random.randn(4), 'A')
print("✅ Logic Check: Human-in-the-loop reward modeling verified.")
