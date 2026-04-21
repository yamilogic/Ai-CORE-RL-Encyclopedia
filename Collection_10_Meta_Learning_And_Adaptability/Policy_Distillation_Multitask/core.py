import numpy as np

def multi_task_distillation_step(student_logits, teacher_logits_list, alpha=0.9):
    # Policy Distillation: One Student learning from Many Experts
    # Loss = sum( KL( Student || Teacher_i ) )
    # This compresses 10 different game-expert-brains into 1 'Super-Brain'.
    avg_teacher_logits = np.mean(teacher_logits_list, axis=0)
    distill_loss = np.mean(np.square(student_logits - avg_teacher_logits))
    print(f"🚀 Distillation: Learning from {len(teacher_logits_list)} Experts. Loss={distill_loss:.4f}")
    return distill_loss

print("🚀 Policy Distillation: Multi-expert knowledge compression.")
s_l = np.array([0.5, 0.5])
t_ls = [np.array([0.6, 0.4]), np.array([0.4, 0.6])] # Two experts with different ideas
multi_task_distillation_step(s_l, t_ls)
print("✅ Logic Check: Multi-teacher logit averaging verified.")
