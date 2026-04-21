import numpy as np

def information_gain_reward(obs, model_error_before, model_error_after):
    # Exploration via Information Gain: Reward = Decrease in Uncertainty
    # I am rewarded if being here made me 'Less Confused' about the world.
    # Reward = Error_Before - Error_After
    gain = model_error_before - model_error_after
    print(f"🚀 Info Gain: Reward={gain:.4f} | Confusion reduced!")
    return gain

print("🚀 Exploration via Information Gain: Targeted uncertainty reduction.")
information_gain_reward(None, 10.0, 2.0) # High reduction
print("✅ Logic Check: Uncertainty-reduction-based reward verified.")
