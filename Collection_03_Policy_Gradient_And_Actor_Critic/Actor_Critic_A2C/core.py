import numpy as np

def a2c_step(s, w_actor, w_critic):
    # Actor: Decides Action | Critic: Evaluates State
    prob = np.exp(np.dot(s, w_actor)) / np.sum(np.exp(np.dot(s, w_actor)))
    value = np.dot(s, w_critic)
    
    # TD Error (Advantage): How much better was the action than expected?
    advantage = (10 + 0.99 * 5.0) - value # r + gamma*V(ns) - V(s)
    
    print(f"🚀 A2C: Advantage = {advantage:.2f} | Action Prob = {prob}")
    return advantage

print("🚀 Actor-Critic (A2C): The Coach (Critic) and the Athlete (Actor).")
a2c_step(np.random.randn(4), np.random.randn(4, 2), np.random.randn(4))
print("✅ Logic Check: Advantage calculated for policy update.")
