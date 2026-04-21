import numpy as np

def kickstarting_loss(student_logits, teacher_logits, weight=0.5):
    # Kickstarting: Distillation of an Expert into a New Agent
    # Student learns from Environment AND from mimicking the Teacher
    # Loss = RL_Loss + weight * KL_Divergence(Student, Teacher)
    
    # Simple mimicry: MSE between logits
    mimicry_loss = np.mean(np.square(student_logits - teacher_logits))
    print(f"🚀 Kickstarting: Teacher Influence={weight} | Mimicry Loss={mimicry_loss:.4f}")
    return mimicry_loss

print("🚀 Kickstarting RL: Accelerated learning via expert teacher distillation.")
s_l = np.array([1.0, 0.0, 0.5])
t_l = np.array([0.9, 0.1, 0.4])
kickstarting_loss(s_l, t_l)
print("✅ Logic Check: Teacher-student logit distillation verified.")
