import numpy as np

def world_model(s, a):
    # The agent's "Imagination": predicting the next state
    # s_next = s + a + some_dynamics
    return s + a + np.random.normal(0, 0.1, s.shape)

def imagine_and_plan(s):
    # Instead of acting in the world, the agent "Dreams" 10 steps ahead
    path = [s]
    for _ in range(5):
        s = world_model(s, np.random.randn(2))
        path.append(s)
    return path

print("🚀 Model-Based RL: Learning to 'Dream' and Plan the future.")
path = imagine_and_plan(np.array([0.0, 0.0]))
print(f"✅ Imagined Path: {len(path)} steps simulated in the agent's mind.")
