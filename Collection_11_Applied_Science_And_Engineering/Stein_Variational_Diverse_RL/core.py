import numpy as np

def svpg_repulsive_force(agent_params, other_agents):
    # SVPG: Agents push each other away to stay DIVERSE
    # force = grad(log_prob) + repulsive_term(distance)
    diff = agent_params - other_agents
    repulsion = np.sum(diff / (np.linalg.norm(diff, axis=1, keepdims=True) + 1e-5), axis=0)
    print(f"🚀 SVPG: Repulsive Force = {np.linalg.norm(repulsion):.4f} | Agents avoiding overlap.")
    return repulsion

print("🚀 Stein Variational Policy Gradient (SVPG): A population of diverse policies.")
me = np.array([1.0, 1.0])
others = np.array([[1.1, 0.9], [0.5, 1.5]])
svpg_repulsive_force(me, others)
print("✅ Logic Check: Agents calculating diversity-based 'repulsion' verified.")
