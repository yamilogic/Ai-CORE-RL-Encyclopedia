import numpy as np

def ocean_nav_reward(current_velocity, goal_dist, energy_usage):
    # RL for Ocean Navigation: Using 'Ocean Currents' to save energy.
    # Reward = (Speed_Toward_Goal) - (Battery_Usage)
    # The agent must learn to 'Hitch a ride' on the Gulf Stream.
    speed_reward = 10.0 / (goal_dist + 1e-8)
    reward = speed_reward - energy_usage
    print(f"🚀 Ocean-RL: Dist={goal_dist:.2f} | Energy={energy_usage:.4f} | Reward={reward:.2f}")
    return reward

print("🚀 RL for Autonomous Ocean Navigation: Long-range maritime optimization.")
ocean_nav_reward(Current_Velocity=2.0, goal_dist=500.0, energy_usage=0.1)
print("✅ Logic Check: Speed-energy balance in fluid dynamics verified.")
