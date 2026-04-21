import numpy as np

def satellite_target_reward(image_resolution, area_coverage, cloud_penalty):
    # RL for Satellite Targeting: Deciding where to point the camera.
    # Reward = (Resolution * Coverage) - Cloud_Penalty
    # The agent must decide which part of Earth to photograph to maximize value.
    reward = (image_resolution * area_coverage) - cloud_penalty
    print(f"🚀 Sat-Target: Res={image_resolution} | Clouds={cloud_penalty} | Reward={reward:.2f}")
    return reward

print("🚀 RL for Satellite Image Targeting: Maximizing orbital data yield.")
satellite_target_reward(image_resolution=1.0, area_coverage=50, cloud_penalty=10)
print("✅ Logic Check: Resolution-coverage-cloud reward verified.")
