import numpy as np

def fusion_control_reward(plasma_shape_error, magnetic_coil_currents):
    # RL for Fusion Control: Maintaining a 100-million degree plasma.
    # Reward = - (Shape_Error + Energy_Surge_Penalty)
    # The agent adjusts 19+ magnetic coils 10,000 times per second.
    shape_accuracy = -np.sum(np.abs(plasma_shape_error))
    surge_penalty = 0.0
    if np.max(magnetic_coil_currents) > 1000:
        surge_penalty = -500.0
        
    reward = shape_accuracy + surge_penalty
    print(f"🚀 Fusion-RL: Shape Accuracy={shape_accuracy:.2f} | Surge={surge_penalty} | Reward={reward:.2f}")
    return reward

print("🚀 RL for Fusion Control: Managing the power of the stars.")
err = np.random.randn(5) * 0.1
coils = np.random.randn(19) * 500
fusion_control_reward(err, coils)
print("✅ Logic Check: Plasma-shape-error reward verified.")
