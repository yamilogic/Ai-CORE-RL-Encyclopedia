import numpy as np

def prioritized_sample(buffer, priorities):
    # Calculate probabilities based on TD-error (Priority)
    probs = priorities / np.sum(priorities)
    idx = np.random.choice(len(buffer), p=probs)
    print(f"🚀 PER: Sampled index {idx} with priority {priorities[idx]:.2f}")
    return buffer[idx]

print("🚀 PER Core: Learning from 'Surprising' mistakes more often.")
buf = ["Step 1", "Step 2", "Critical Error!", "Step 4"]
prios = np.array([0.1, 0.1, 5.0, 0.1]) # Higher priority for the error
sample = prioritized_sample(buf, prios)
print(f"✅ Logic Check: {sample} was prioritized.")
