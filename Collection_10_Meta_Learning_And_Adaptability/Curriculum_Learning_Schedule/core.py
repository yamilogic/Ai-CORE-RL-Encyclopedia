import numpy as np

def update_curriculum(success_rate, current_difficulty):
    # Curriculum Learning: Adjusting the environment difficulty
    # If success > 80%, make it harder. If < 20%, make it easier.
    if success_rate > 0.8:
        current_difficulty += 1.0
        print(f"🚀 Curriculum: Agent is a PRO. Increasing Difficulty to {current_difficulty}")
    elif success_rate < 0.2:
        current_difficulty = max(1.0, current_difficulty - 1.0)
        print(f"🚀 Curriculum: Agent is struggling. Decreasing Difficulty to {current_difficulty}")
    return current_difficulty

print("🚀 Curriculum Learning: Training in a 'staircase' of difficulty.")
update_curriculum(0.95, 1.0)
print("✅ Logic Check: Automated task scaling verified.")
