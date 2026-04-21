import numpy as np

class GridEnv:
    def __init__(self, size=5):
        self.size, self.goal, self.walls = size, (size-1, size-1), [(1,1), (2,1), (3,1), (1,3), (2,3)]
        self.reset()
    def reset(self): self.pos = [0,0]; return 0
    def step(self, a):
        dr, dc = [(-1,0),(1,0),(0,-1),(0,1)][a]
        nr, nc = self.pos[0]+dr, self.pos[1]+dc
        if 0<=nr<self.size and 0<=nc<self.size and (nr,nc) not in self.walls: self.pos = [nr,nc]
        done = tuple(self.pos) == self.goal
        return self.pos[0]*self.size+self.pos[1], 10 if done else -0.1, done

def train(eps=500, a=0.1, g=0.95):
    env, Q = GridEnv(), np.zeros((25, 4))
    e, decay = 1.0, 0.99
    for _ in range(eps):
        s, done = env.reset(), False
        while not done:
            act = np.random.randint(4) if np.random.rand() < e else np.argmax(Q[s])
            ns, r, done = env.step(act)
            Q[s,act] += a * (r + g*np.max(Q[ns]) - Q[s,act])
            s = ns
        e = max(0.01, e * decay)
    return Q
