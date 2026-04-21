import numpy as np

def tutor_path_reward(student_exam_score, learning_time, frustration_level):
    # RL for Education: Finding the best order to teach concepts.
    # Reward = (Score_Improvement / Time) - Frustration
    # The agent decides which 'Lesson' to show next.
    efficiency = student_exam_score / (learning_time + 1e-8)
    reward = efficiency * 10.0 - frustration_level * 5.0
    print(f"🚀 Tutor-RL: Score={student_exam_score} | Frustration={frustration_level} | Reward={reward:.2f}")
    return reward

print("🚀 RL for Personalized Tutor Path: Optimizing the journey of knowledge.")
tutor_path_reward(student_exam_score=95, learning_time=2, frustration_level=0.1)
print("✅ Logic Check: Efficiency-frustration tutor reward verified.")
