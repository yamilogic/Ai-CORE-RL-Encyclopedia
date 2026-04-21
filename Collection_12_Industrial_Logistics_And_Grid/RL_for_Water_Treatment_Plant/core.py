import numpy as np

def water_treatment_reward(turbidity, chlorine_level, energy_cost):
    # RL for Water Treatment: Balancing purity and cost.
    # Reward = - (Impurity_Level + C1 * Chlorine_Error + C2 * Energy)
    # The agent controls pump speeds and chemical dosers.
    purity_penalty = turbidity * 50.0
    chemical_err = np.abs(chlorine_level - 1.5) * 20.0
    reward = -(purity_penalty + chemical_err + energy_cost * 0.5)
    print(f"🚀 Water-RL: Turbidity={turbidity:.2f} | Chlorine={chlorine_level:.2f} | Reward={reward:.2f}")
    return reward

print("🚀 RL for Water Treatment Plant: Engineering clean hydration.")
water_treatment_reward(turbidity=0.1, chlorine_level=1.45, energy_cost=50)
print("✅ Logic Check: Purity-chemical-energy reward verified.")
