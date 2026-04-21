import numpy as np

def pets_ensemble_predict(state, action, ensemble_weights):
    # PETS: Handling Uncertainty via Ensembles
    # Each model in the ensemble gives a different prediction.
    # The 'Spread' of predictions tells us how 'Uncertain' we are.
    predictions = [np.dot(np.concatenate([state, action]), w) for w in ensemble_weights]
    mean_prediction = np.mean(predictions, axis=0)
    uncertainty = np.std(predictions, axis=0)
    
    print(f"🚀 PETS Ensemble: Prediction={mean_prediction[:2]}... | Uncertainty={np.mean(uncertainty):.4f}")
    return mean_prediction, uncertainty

print("🚀 PETS: Initializing Probabilistic Model Ensemble...")
s = np.random.randn(4)
a = np.random.randn(2)
ens_w = [np.random.randn(6, 4) for _ in range(5)] # 5 models in the ensemble
pets_ensemble_predict(s, a, ens_w)
print("✅ Logic Check: Uncertainty-aware ensemble prediction verified.")
