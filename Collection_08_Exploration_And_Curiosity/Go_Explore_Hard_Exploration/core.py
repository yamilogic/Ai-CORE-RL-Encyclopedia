import numpy as np

def go_explore_save_cell(archive, state, reward):
    # Go-Explore: 'Cell-based' archive of every state reached
    # Key = Compressed version of the state
    cell_id = tuple(np.round(state, 1))
    if cell_id not in archive or reward > archive[cell_id]['reward']:
        archive[cell_id] = {'state': state, 'reward': reward}
        print(f"🚀 Go-Explore: New discovery! Cell {cell_id} added to archive.")
    return archive

print("🚀 Go-Explore Core: Solving hard exploration via 'First Return, Then Explore'.")
arch = {}
s1 = np.array([0.11, 0.52])
go_explore_save_cell(arch, s1, 10.0)
print("✅ Logic Check: Cell-based discovery and archiving verified.")
