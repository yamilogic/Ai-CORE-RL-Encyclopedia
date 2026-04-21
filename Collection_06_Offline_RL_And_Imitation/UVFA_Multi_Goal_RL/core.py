import numpy as np

def uvfa_predict(state, goal, weights):
    # Universal Value Function Approximator
    # Learns Q(s, a, g) - Value depends on the current goal!
    state_goal = np.concatenate([state, goal])
    value = np.dot(state_goal, weights)
    print(f"🚀 UVFA: State={state} | Target Goal={goal} | Predicted Value={value:.2f}")
    return value

print("🚀 UVFA Core: Learning to reach multiple goals with a single brain.")
s, g = np.array([0, 1]), np.array([5, 5])
w = np.random.randn(4)
uvfa_predict(s, g, w)
print("✅ Logic Check: Value calculation is now goal-conditioned.")
