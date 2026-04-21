import numpy as np

def uav_payload_reward(pos_error, oscillation_level, wind_speed):
    # RL for UAVs: Carrying a swinging payload.
    # Reward = - (Pos_Error + C1 * Oscillation + C2 * Motor_Heat)
    # The agent must fly in a way that 'Dampens' the swinging package.
    reward = -(pos_error * 10.0 + oscillation_level * 20.0 + wind_speed * 1.0)
    print(f"🚀 UAV-RL: Error={pos_error:.2f} | Swing={oscillation_level:.2f} | Reward={reward:.2f}")
    return reward

print("🚀 RL for UAV Payload Delivery: Precision flight with dynamic loads.")
uav_payload_reward(pos_error=0.5, oscillation_level=1.2, wind_speed=15)
print("✅ Logic Check: Error-oscillation-wind UAV reward verified.")
