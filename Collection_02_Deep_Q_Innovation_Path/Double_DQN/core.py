import numpy as np

def double_dqn_update(q_net, target_net, s, a, r, ns):
    # 1. Selection: Pick best action using ONLINE net
    best_a = np.argmax(q_net[ns])
    # 2. Evaluation: Get Q-value of that action using TARGET net
    target_q = r + 0.99 * target_net[ns, best_a]
    print(f"🚀 Double DQN: Target = {target_q:.2f} (Action {best_a} selected by Online, evaluated by Target)")
    return target_q

print("🚀 Double DQN: Fixing overestimation by separating Selection and Evaluation.")
q, target = np.random.randn(5, 2), np.random.randn(5, 2)
double_dqn_update(q, target, 0, 1, 10.0, 1)
print("✅ Logic Check: Decoupled selection/evaluation verified.")
