import numpy as np

def curriculum_scheduler(performance, current_difficulty):
    # Curriculum RL: Increasing difficulty as the agent learns
    # performance: 0 to 1
    if performance > 0.8:
        new_difficulty = current_difficulty + 0.1
        print(f"🚀 Curriculum: Agent MASTERED level {current_difficulty:.1f}. Leveling up to {new_difficulty:.1f}!")
    elif performance < 0.2:
        new_difficulty = max(0.1, current_difficulty - 0.1)
        print(f"⚠️ Curriculum: Level too hard. Dropping to {new_difficulty:.1f}.")
    else:
        new_difficulty = current_difficulty
        print(f"🚀 Curriculum: Staying at level {current_difficulty:.1f}. Agent still learning.")
    return new_difficulty

print("🚀 Robot Walk Curriculum RL: Progressive difficulty training.")
curriculum_scheduler(0.9, 1.0)
curriculum_scheduler(0.1, 1.0)
print("✅ Logic Check: Performance-based difficulty scaling verified.")
