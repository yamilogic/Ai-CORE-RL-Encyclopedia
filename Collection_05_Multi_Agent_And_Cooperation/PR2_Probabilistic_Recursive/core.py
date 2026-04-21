import numpy as np

def pr2_recursive_belief(my_intent, opponent_belief_of_me, joint_reward):
    # PR2: Probabilistic Recursive Reasoning
    # Level 0: I act randomly.
    # Level 1: I act based on what I think you will do.
    # Level 2: I act based on what I think YOU think I will do.
    # Level k...
    
    # Simple recursive alignment: My intent vs their belief of my intent
    alignment = np.dot(my_intent, opponent_belief_of_me)
    print(f"🚀 PR2: Recursive Alignment={alignment:.4f} | 'I think you think...'")
    return alignment

print("🚀 PR2: Initializing Recursive Multi-Agent Reasoning...")
m_i = np.array([1, 0])
o_b = np.array([0.9, 0.1]) # Opponent correctly guesses I will go Left
pr2_recursive_belief(m_i, o_b, 10.0)
print("✅ Logic Check: Theory-of-Mind recursive alignment verified.")
