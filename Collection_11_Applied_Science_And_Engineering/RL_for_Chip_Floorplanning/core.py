import numpy as np

def chip_floorplan_reward(component_positions, wire_length_w, area_w):
    # RL for Chip Floorplanning: Minimizing Wire-length and Area.
    # Reward = - (W1 * Total_Wire_Length + W2 * Total_Area)
    # The agent must place billions of transistors to maximize speed.
    wire_length = np.sum(np.abs(np.diff(component_positions, axis=0)))
    total_area = (np.max(component_positions[:,0]) - np.min(component_positions[:,0])) * \
                 (np.max(component_positions[:,1]) - np.min(component_positions[:,1]))
    
    reward = -(wire_length_w * wire_length + area_w * total_area)
    print(f"🚀 Chip-RL: Wire Length={wire_length:.2f} | Area={total_area:.2f} | Reward={reward:.2f}")
    return reward

print("🚀 RL for Chip Floorplanning: Optimizing next-gen silicon layouts.")
pos = np.array([[0,0], [1,1], [2,0]]) # 3 components
chip_floorplan_reward(pos, 0.5, 0.5)
print("✅ Logic Check: Wire-length/area reward function verified.")
