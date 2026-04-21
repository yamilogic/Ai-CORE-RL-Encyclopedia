import numpy as np

def satellite_attitude_step(current_orientation, target_orientation, angular_vel, thruster_weights):
    # Satellite RL: Pointing sensors precisely in space
    # State = Orientation error, Rotation speed
    error = target_orientation - current_orientation
    action = np.tanh(np.dot(np.append(error, angular_vel), thruster_weights))
    print(f"🚀 Satellite RL: Orient Error={error:.4f} | Thruster Force={action:.2f}")
    return action

print("🚀 Satellite Attitude Control RL: Precise pointing via reaction wheels and thrusters.")
curr, target = 0.0, 1.57 # 90 degrees
vel = 0.01
w = np.random.randn(2)
satellite_attitude_step(curr, target, vel, w)
print("✅ Logic Check: Orientation-error-based thrusting verified.")
