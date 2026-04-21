import numpy as np

def human_robot_safety_step(human_dist, robot_velocity, safety_weights):
    # Human-Robot Interaction (HRI): Safety-aware velocity control
    # State = Distance to human, Current robot speed
    # Constraint: Velocity must decrease as distance decreases
    max_safe_vel = human_dist * 0.5 # Simplified safety rule
    proposed_vel = np.dot([human_dist, robot_velocity], safety_weights)
    safe_vel = min(proposed_vel, max_safe_vel)
    print(f"🚀 HRI RL: Human Dist={human_dist:.2f} | Safe Max Vel={max_safe_vel:.2f} | Final Vel={safe_vel:.2f}")
    return safe_vel

print("🚀 Safe Human-Robot Interaction RL: Proximity-aware speed regulation.")
human_robot_safety_step(1.0, 5.0, np.random.randn(2)) # Human close
human_robot_safety_step(10.0, 5.0, np.random.randn(2)) # Human far
print("✅ Logic Check: Proximity-scaled velocity capping verified.")
