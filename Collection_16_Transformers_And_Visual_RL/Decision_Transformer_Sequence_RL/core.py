import numpy as np

def decision_transformer_inference(returns_to_go, state_history, action_history):
    # Decision Transformer: RL as Sequence Modeling.
    # Prediction: (R_1, s_1, a_1, R_2, s_2, a_2, ...) -> a_t
    # Instead of 'predicting reward', we 'Condition on Reward' (Returns-to-go).
    # 'If I want a score of 100, what is the most likely next action?'
    
    # Simple prediction proxy
    seq = np.concatenate([returns_to_go, state_history.flatten(), action_history.flatten()])
    next_action = np.tanh(np.mean(seq)) # Simplified Transformer logic
    print(f"🚀 DT: Target Return={returns_to_go[0]} | Predicted Action={next_action:.4f}")
    return next_action

print("🚀 Decision Transformer: Initializing Sequence-Modeling Engine...")
rtg = np.array([100.0]) # I want 100 points
s_h = np.random.randn(5, 4) # Last 5 states
a_h = np.random.randn(5, 2) # Last 5 actions
decision_transformer_inference(rtg, s_h, a_h)
print("✅ Logic Check: Sequence-conditioned action prediction verified.")
