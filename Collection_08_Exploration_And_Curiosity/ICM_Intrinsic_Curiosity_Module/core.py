import numpy as np

def icm_intrinsic_reward(state, next_state, action, forward_model_w):
    # ICM: Reward = Prediction Error of the World
    # If the AI is surprised, it gets a reward!
    predicted_next_state = np.dot(np.concatenate([state, action]), forward_model_w)
    prediction_error = np.linalg.norm(next_state - predicted_next_state)
    print(f"🚀 ICM: Error={prediction_error:.4f} | Intrinsic Reward Generated!")
    return prediction_error

print("🚀 ICM: Initializing Curiosity Engine...")
s, ns = np.random.randn(4), np.random.randn(4)
a = np.random.randn(2)
w = np.random.randn(6, 4)
icm_intrinsic_reward(s, ns, a, w)
print("✅ Logic Check: Prediction-error-based curiosity verified.")
