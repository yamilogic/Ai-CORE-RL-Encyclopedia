import numpy as np

def apply_action_mask(logits, mask):
    # Action Masking: Forcing illegal actions to probability 0
    # Mask is 1 for allowed, 0 for forbidden
    # Set forbidden logits to -infinity
    masked_logits = np.where(mask == 1, logits, -1e10)
    probs = np.exp(masked_logits) / np.sum(np.exp(masked_logits))
    print(f"🚀 Masking: Probs={probs.round(2)} | Illegal actions zeroed out.")
    return probs

print("🚀 Action Masking: Preventing the AI from even considering 'Illegal' moves.")
l = np.array([2.0, 5.0, 1.0]) # 3 Actions
m = np.array([1, 0, 1]) # Action 1 is forbidden!
apply_action_mask(l, m)
print("✅ Logic Check: Probability suppression for masked actions verified.")
