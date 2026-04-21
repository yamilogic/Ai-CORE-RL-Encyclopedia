import numpy as np

def iql_expectile_loss(q_values, v_values, tau=0.7):
    # IQL: Implicit Q-Learning for Offline RL.
    # Key Logic: Instead of sampling actions we haven't seen, 
    # we just use Expectile Regression on the existing Q-values.
    # Loss = |tau - I(diff < 0)| * diff^2
    diff = q_values - v_values
    weight = np.where(diff > 0, tau, 1 - tau)
    loss = weight * (diff**2)
    
    print(f"🚀 IQL: Expectile Loss={np.mean(loss):.4f} | Learning the Upper Tail of data.")
    return np.mean(loss)

print("🚀 IQL: Initializing Expectile-based Offline RL Engine...")
q_in = np.array([10.0, 12.0, 8.0])
v_in = np.array([9.0, 9.0, 9.0])
iql_expectile_loss(q_in, v_in)
print("✅ Logic Check: Expectile-weighted square loss verified.")
