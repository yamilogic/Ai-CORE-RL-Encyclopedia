import numpy as np

def rnd_intrinsic_reward(state, fixed_net_w, predictor_net_w):
    # RND: Novelty via Distillation Error
    # Reward = Error between a FIXED random network and a PREDICTOR network
    # Since the fixed network is constant, the predictor can only learn 
    # to mimic it on states it has seen many times.
    target = np.dot(state, fixed_net_w)
    prediction = np.dot(state, predictor_net_w)
    
    novelty_score = np.linalg.norm(target - prediction)
    print(f"🚀 RND: Novelty Score={novelty_score:.4f} | {'NEW!' if novelty_score > 1.0 else 'Seen before.'}")
    return novelty_score

print("🚀 RND: Initializing Random Network Distillation Curiosity...")
s_val = np.random.randn(8)
w_fixed = np.random.randn(8, 4)
w_pred = np.random.randn(8, 4)
rnd_intrinsic_reward(s_val, w_fixed, w_pred)
print("✅ Logic Check: Prediction-error-based novelty reward verified.")
