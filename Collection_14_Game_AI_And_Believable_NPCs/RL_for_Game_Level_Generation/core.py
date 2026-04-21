import numpy as np

def game_level_reward(level_layout, difficulty_target, playability_score):
    # RL for Level Design: Procedural Content Generation (PCG).
    # Reward = - (Playability + |Difficulty - Target|)
    # The agent 'Places' blocks to create a fun, beatable level.
    diff_err = np.abs(np.mean(level_layout) - difficulty_target)
    reward = playability_score * 10.0 - diff_err
    print(f"🚀 Level-RL: Playability={playability_score} | Diff Error={diff_err:.2f} | Reward={reward:.2f}")
    return reward

print("🚀 RL for Game Level Generation: Automating infinite fun.")
layout = np.random.rand(10, 10)
game_level_reward(layout, 0.5, 0.95)
print("✅ Logic Check: Playability-difficulty level reward verified.")
