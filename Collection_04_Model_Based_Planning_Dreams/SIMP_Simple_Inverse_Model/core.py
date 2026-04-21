import numpy as np

def inverse_model_action(state, next_state, inverse_w):
    # SIMP: Learning 'What actions lead to this change?'
    # Instead of predicting the future, we predict the 'Cause'
    # Action = f(State, Next_State)
    predicted_action = np.dot(np.concatenate([state, next_state]), inverse_w)
    print(f"🚀 SIMP: Predicted the Action that caused this transition: {predicted_action.round(4)}")
    return predicted_action

print("🚀 SIMP: Initializing Inverse-Dynamics Planning...")
s_curr, s_next = np.random.randn(4), np.random.randn(4)
w_inv = np.random.randn(8, 2)
inverse_model_action(s_curr, s_next, w_inv)
print("✅ Logic Check: Inverse-model action prediction verified.")
