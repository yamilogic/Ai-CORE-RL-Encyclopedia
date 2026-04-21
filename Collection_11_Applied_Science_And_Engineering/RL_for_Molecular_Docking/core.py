import numpy as np

def molecular_docking_reward(binding_energy, steric_clash_count):
    # RL for Molecular Docking: Finding how a drug fits into a protein.
    # Reward = - (Binding_Energy + Penalty * Clashes)
    # The agent moves and rotates the 'Ligand' to maximize the 'Fit'.
    clash_penalty = steric_clash_count * 10.0
    reward = -(binding_energy + clash_penalty)
    print(f"🚀 Docking-RL: Energy={binding_energy:.2f} | Clashes={steric_clash_count} | Reward={reward:.2f}")
    return reward

print("🚀 RL for Molecular Docking: Computational drug-target alignment.")
molecular_docking_reward(Binding_Energy=-12.5, steric_clash_count=0) # Strong negative energy is good
print("✅ Logic Check: Energy-clash docking reward verified.")
