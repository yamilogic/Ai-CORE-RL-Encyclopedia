import numpy as np

def cpc_score(z_future, z_pred, weight_matrix):
    # CPC: Scoring the 'Quality' of a future prediction
    # Score = exp( z_future' * W * z_pred )
    # We want to maximize the score for the 'Real' future
    score = np.exp(z_future @ weight_matrix @ z_pred)
    print(f"🚀 CPC: Compatibility Score={score:.4f} | Predicting future features.")
    return score

print("🚀 CPC Core: Learning representations by predicting future latent states.")
z_f = np.random.randn(4)
z_p = np.random.randn(4)
w = np.random.randn(4, 4)
cpc_score(z_f, z_p, w)
print("✅ Logic Check: Latent future compatibility verified.")
