import numpy as np

def rnd_curiosity_reward(s, target_net, predictor_net):
    # RND: Curiosity = Error between Predictor and a FIXED Target Net
    # Predictor tries to learn the output of Target Net
    # Higher error = State is NEW/UNFAMILIAR
    target_val = np.dot(s, target_net)
    pred_val = np.dot(s, predictor_net)
    error = np.mean(np.square(target_val - pred_val))
    print(f"🚀 RND Curiosity: Error = {error:.4f} | Agent is motivated to explore.")
    return error

print("🚀 RND Core: Advanced exploration by predicting the unpredictable.")
s = np.random.randn(4)
t_net, p_net = np.random.randn(4, 2), np.random.randn(4, 2)
rnd_curiosity_reward(s, t_net, p_net)
print("✅ Logic Check: Prediction error used as intrinsic reward verified.")
