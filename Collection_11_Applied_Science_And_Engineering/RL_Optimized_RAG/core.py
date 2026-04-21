import numpy as np

class RLRAGEnv:
    def __init__(self): self.qs = list(range(10)); self.reset()
    def reset(self): self.q = np.random.choice(self.qs); return self.q
    def step(self, a):
        is_hard = self.q >= 5
        r = 10 if (a==0 and not is_hard) else (8 if a==1 else -5)
        return 0, r, True

def train_rag(eps=500):
    env, Q = RLRAGEnv(), np.zeros((10, 2))
    for _ in range(eps):
        s, done = env.reset(), False
        while not done:
            a = np.random.randint(2) if np.random.rand() < 0.1 else np.argmax(Q[s])
            _, r, done = env.step(a); Q[s, a] += 0.1 * (r - Q[s, a]); s = 0
    return Q

print("🚀 RL-RAG Core (Numpy): Adaptive Retrieval Logic.")
Q = train_rag()
print(f"✅ Strategy Learned: Question 9 (Hard) -> {'Retrieve' if np.argmax(Q[9])==1 else 'Direct'}")
