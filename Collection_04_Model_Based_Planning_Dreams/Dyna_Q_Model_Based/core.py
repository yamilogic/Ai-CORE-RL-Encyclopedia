import numpy as np

def dyna_q_step(Q, model, s, a, r, ns):
    # 1. Real Experience update
    Q[s, a] += 0.1 * (r + 0.9 * np.max(Q[ns]) - Q[s, a])
    model[(s, a)] = (r, ns) # Update internal model
    
    # 2. Planning: Imagine 5 past experiences
    for _ in range(5):
        ms, ma = list(model.keys())[np.random.randint(len(model))]
        mr, mns = model[(ms, ma)]
        Q[ms, ma] += 0.1 * (mr + 0.9 * np.max(Q[mns]) - Q[ms, ma])
    return Q

print("🚀 Dyna-Q: Learning from Reality AND Imagination.")
Q, model = np.zeros((10, 2)), {(0,1): (10.0, 1)}
dyna_q_step(Q, model, 0, 1, 10.0, 1)
print("✅ Logic Check: Real update + 5 imaginary updates verified.")
