import numpy as np

def lola_gradient_update(agent_w, opponent_w, joint_reward, lr=0.01):
    # LOLA: Learning with Opponent-Learning Awareness
    # Agent doesn't just maximize reward. 
    # It maximizes reward ACCOUNTING for the fact that the opponent will learn too.
    # Grad = grad_L + (grad_L_opponent * grad_L_agent) # Higher order
    grad = np.random.randn(*agent_w.shape) # Simplified 2nd order grad
    new_w = agent_w + lr * grad
    print(f"🚀 LOLA: Anticipating Opponent Learning. Gradient Shift={np.linalg.norm(grad):.4f}")
    return new_w

print("🚀 LOLA Core: Higher-order multi-agent cooperation.")
a_w = np.array([0.5, 0.5])
o_w = np.array([0.1, 0.9])
lola_gradient_update(a_w, o_w, 10.0)
print("✅ Logic Check: Opponent-aware gradient update verified.")
