import numpy as np

class MARLGrid:
    def __init__(self, size=5):
        self.size = size
        self.agents = [[0,0], [size-1, size-1]]
        self.goal = [size//2, size//2]

    def step(self, actions):
        rewards = []
        for i, a in enumerate(actions):
            dr, dc = [(-1,0),(1,0),(0,-1),(0,1)][a]
            self.agents[i][0] = np.clip(self.agents[i][0]+dr, 0, self.size-1)
            self.agents[i][1] = np.clip(self.agents[i][1]+dc, 0, self.size-1)
            dist = np.abs(self.agents[i][0]-self.goal[0]) + np.abs(self.agents[i][1]-self.goal[1])
            rewards.append(10 if dist == 0 else -0.1)
        return rewards, all(np.array_equal(a, self.goal) for a in self.agents)

print("🚀 MARL Simulation: 2 agents seeking a central goal...")
env = MARLGrid()
for _ in range(3):
    actions = [np.random.randint(4) for _ in range(2)]
    rewards, done = env.step(actions)
    print(f"Agents at {env.agents} | Rewards: {rewards}")
