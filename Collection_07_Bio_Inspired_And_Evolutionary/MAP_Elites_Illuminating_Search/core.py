import numpy as np

class MAPElites:
    """
    MAP-Elites: Quality-Diversity Search.
    Maintains a grid of the 'Best' agents for every possible behavior.
    """
    def __init__(self, grid_size=10):
        self.grid = {} # (behavior_x, behavior_y) -> (genome, fitness)

    def add_to_grid(self, genome, fitness, b_x, b_y):
        cell = (b_x, b_y)
        if cell not in self.grid or fitness > self.grid[cell][1]:
            self.grid[cell] = (genome, fitness)
            print(f"🚀 MAP-Elites: NEW ELITE found in cell {cell}! Fitness={fitness:.2f}")

print("🚀 MAP-Elites: Initializing Quality-Diversity Map...")
me = MAPElites()
me.add_to_grid("DNA_1", 10.0, 1, 1)
me.add_to_grid("DNA_2", 15.0, 1, 1) # Overwrites because fitness is higher
me.add_to_grid("DNA_3", 5.0, 2, 2)  # New cell
print(f"✅ Logic Check: Map occupancy={len(me.grid)} cells.")
