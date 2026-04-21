import numpy as np

def reinforce_update(prob, reward, baseline):
    # Standard REINFORCE: log_prob * reward
    # With Baseline: log_prob * (reward - baseline)
    advantage = reward - baseline
    update = np.log(prob) * advantage
    print(f"🚀 REINFORCE: Reward={reward} | Baseline={baseline} | Update Scaling={advantage:.2f}")
    return update

print("🚀 REINFORCE with Baseline: Reducing variance in Policy Gradients.")
reinforce_update(0.6, 10.0, 8.5)
print("✅ Logic Check: Update depends on how much BETTER the reward was than average.")
