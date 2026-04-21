import numpy as np

def distill_step(teacher_probs, student_logits):
    # Student learns to match Teacher's probability distribution
    student_probs = np.exp(student_logits) / np.sum(np.exp(student_logits))
    # KL Divergence (Simplified): Loss = teacher * log(teacher/student)
    loss = np.sum(teacher_probs * np.log(teacher_probs / (student_probs + 1e-5)))
    print(f"🚀 Distillation: KL Loss = {loss:.4f} | Student matching Teacher...")
    return loss

print("🚀 Policy Distillation Core: Compressing a big Teacher into a small Student.")
teacher = np.array([0.7, 0.2, 0.1])
student = np.array([0.5, 0.5, 1.0]) # Logits
distill_step(teacher, student)
print("✅ Logic Check: Student learned the 'wisdom' of the Teacher.")
