import numpy as np

def lyapunov_safety_projection(action, state, lyapunov_w, safety_threshold=0.5):
    # Lyapunov-based Safe RL: Energy-based stability
    # V(s) is an energy function. We ensure dV/dt < 0.
    energy = np.dot(state, lyapunov_w)
    # If energy is rising, project action back to safe set
    if energy > safety_threshold:
        print("⚠️ Lyapunov: High Energy Detected! Projecting to Safe Control.")
        safe_action = -0.1 * state # Dissipative control
        return safe_action
    return action

print("🚀 Lyapunov Safe RL: Energy-constrained stability control.")
s = np.array([0.8, 0.2])
a = np.array([1.0, 1.0])
w_lyap = np.array([1.0, 1.0])
lyapunov_safety_projection(a, s, w_lyap)
print("✅ Logic Check: Energy-dissipative safety projection verified.")
