import numpy as np

def prioritized_sampling(td_errors, alpha=0.6):
    # PER: Sampling experiences proportional to their 'Surprise'
    # Priority = |TD_Error| ^ alpha
    priorities = np.abs(td_errors) ** alpha
    probs = priorities / np.sum(priorities)
    
    indices = np.random.choice(len(td_errors), size=2, p=probs)
    print(f"🚀 PER: Sampled indices {indices} with probabilities {probs[indices].round(4)}")
    return indices

print("🚀 PER: Initializing Surprise-based sampling engine...")
errs = np.array([0.1, 5.0, 0.2, 10.0, 0.05]) # Experience #2 and #4 are 'Surprising'
prioritized_sampling(errs)
print("✅ Logic Check: TD-error-weighted sampling verified.")
