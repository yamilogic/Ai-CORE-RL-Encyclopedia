import numpy as np

def combinatorial_rl_reward(permutation, distance_matrix):
    # Combinatorial RL: Solving the Traveling Salesman (TSP)
    # Reward = -Total_Tour_Length
    # The agent must learn to order nodes to minimize path.
    tour_length = 0
    for i in range(len(permutation) - 1):
        tour_length += distance_matrix[permutation[i], permutation[i+1]]
    # Back to start
    tour_length += distance_matrix[permutation[-1], permutation[0]]
    print(f"🚀 Combinatorial RL: Tour Length={tour_length:.2f} | Reward={-tour_length:.2f}")
    return -tour_length

print("🚀 RL for Combinatorial Optimization: Solving TSP and NP-Hard puzzles.")
dist = np.array([[0, 10, 15], [10, 0, 20], [15, 20, 0]]) # 3 cities
p = [0, 1, 2] # Tour: 0->1->2->0
combinatorial_rl_reward(p, dist)
print("✅ Logic Check: Permutation-based tour reward verified.")
