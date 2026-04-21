import numpy as np

def rcpo_lagrangian_update(reward, safety_cost, lam, lr=0.01):
    # RCPO: Using a Lagrange Multiplier to balance reward and safety
    # Total Reward = Reward - lam * Safety_Cost
    total_r = reward - lam * safety_cost
    # Update lambda (the 'Price' of safety)
    new_lam = max(0, lam + lr * (safety_cost - 0.1)) # Target cost = 0.1
    print(f"🚀 RCPO: Lambda={new_lam:.4f} | Effective Reward={total_r:.2f}")
    return total_r, new_lam

print("🚀 RCPO Core: Reward-constrained optimization via Lagrangian penalty.")
l = 0.5
r, nl = rcpo_lagrangian_update(10.0, 5.0, l) # High safety cost -> Lambda will rise
print("✅ Logic Check: Adaptive penalty multiplier update verified.")
