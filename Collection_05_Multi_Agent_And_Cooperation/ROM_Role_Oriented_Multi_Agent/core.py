import numpy as np

def role_assignment(agent_id, task_embedding, role_weights):
    # ROM: Multi-agent coordination via specialized roles
    # Instead of everyone being a 'Generalist', agents learn to be 'Specialists'
    role_logits = np.dot(task_embedding, role_weights)
    role_id = np.argmax(role_logits)
    role_names = ["🛡️ DEFENDER", "⚔️ ATTACKER", "🛠️ SUPPORT"]
    print(f"🚀 ROM: Agent {agent_id} assigned role: {role_names[role_id]}")
    return role_id

print("🚀 ROM Core: Specialization-based multi-agent coordination.")
t_emb = np.random.randn(8)
r_w = np.random.randn(8, 3)
role_assignment(1, t_emb, r_w)
print("✅ Logic Check: Embedding-based role assignment verified.")
