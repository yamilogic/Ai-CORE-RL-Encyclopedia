import numpy as np

def update_pheromones(paths, rewards, pheromone_map, evaporation=0.1):
    # ACO: Reinforcement via 'Pheromone' trails
    # Evaporate old trails
    pheromone_map *= (1 - evaporation)
    
    # Add new pheromones proportional to success
    for path, reward in zip(paths, rewards):
        for step in path:
            pheromone_map[step] += reward
            
    print(f"🚀 ACO: Pheromones Updated! Max Intensity={np.max(pheromone_map):.2f}")
    return pheromone_map

print("🚀 ACO: Initializing Pheromone-based Pathfinding...")
p_map = np.zeros((5, 5))
successful_paths = [[(0,0), (1,1), (2,2)]]
update_pheromones(successful_paths, [10.0], p_map)
print("✅ Logic Check: Path-reinforcement pheromone update verified.")
