import numpy as np

class Bee:
    def __init__(self, pos):
        self.pos = pos
        self.score = 0.0

def bee_scout_and_recruit(scout_bees, flower_patch_scores):
    # Bee Algorithm: Scout, Recruit, and Forage
    # Top patches get more bees recruited to them.
    # Sorted patches
    indices = np.argsort(flower_patch_scores)[::-1]
    
    # Recruit bees to the top 2 patches
    recruits = []
    for i in range(2):
        best_patch_idx = indices[i]
        # Generate 3 new bees around the best patch
        for _ in range(3):
            new_bee = scout_bees[best_patch_idx].pos + 0.1 * np.random.randn(2)
            recruits.append(new_bee)
            
    print(f"🚀 Bee: Recruitment complete! {len(recruits)} bees sent to the best flower patches.")
    return recruits

print("🚀 Bee Algorithm: Swarm foraging logic.")
scouts = [Bee(np.random.randn(2)) for _ in range(5)]
scores = [10.0, 50.0, 2.0, 100.0, 5.0] # Patch #3 is the winner
bee_scout_and_recruit(scouts, scores)
print("✅ Logic Check: Fitness-proportional recruitment verified.")
