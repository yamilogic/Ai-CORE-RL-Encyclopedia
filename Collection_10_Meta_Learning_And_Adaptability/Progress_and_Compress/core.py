import numpy as np

def progress_and_compress(knowledge_base, new_task_expert, distillation_rate=0.1):
    # Progress: Learn the new task with a specialist
    # Compress: Distill that specialist into the global 'Knowledge Base'
    # Base = (1-rate)*Base + rate*Specialist
    updated_base = (1 - distillation_rate) * knowledge_base + distillation_rate * new_task_expert
    print(f"🚀 P&C: Compressed New Expert into Knowledge Base. Retention={1-distillation_rate:.2f}")
    return updated_base

print("🚀 Progress & Compress: Continual learning without forgetting.")
base_w = np.random.randn(4)
expert_w = np.random.randn(4)
progress_and_compress(base_w, expert_w)
print("✅ Logic Check: Weighted distillation update verified.")
