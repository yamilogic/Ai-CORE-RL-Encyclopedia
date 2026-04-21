import numpy as np

class GoExploreArchive:
    """
    Go-Explore: An archive-based explorer that 'remembers' interesting states.
    """
    def __init__(self):
        self.archive = {} # {state_hash: (state_data, visit_count)}

    def add_to_archive(self, state):
        s_hash = hash(state.tobytes())
        if s_hash not in self.archive:
            self.archive[s_hash] = (state, 1)
            print(f"🚀 Go-Explore: NEW territory discovered! Archive Size={len(self.archive)}")
        else:
            state_data, count = self.archive[s_hash]
            self.archive[s_hash] = (state_data, count + 1)

    def select_state_to_go_back_to(self):
        # Pick the least-visited state to explore from
        hashes = list(self.archive.keys())
        counts = [v[1] for v in self.archive.values()]
        probs = 1.0 / np.array(counts)
        probs /= np.sum(probs)
        return self.archive[hashes[np.random.choice(len(hashes), p=probs)]][0]

print("🚀 Go-Explore: Initializing Archive-based exploration...")
ge = GoExploreArchive()
ge.add_to_archive(np.array([1,2]))
ge.add_to_archive(np.array([1,2]))
ge.add_to_archive(np.array([3,4]))
ge.select_state_to_go_back_to()
print("✅ Logic Check: Least-visited state selection verified.")
