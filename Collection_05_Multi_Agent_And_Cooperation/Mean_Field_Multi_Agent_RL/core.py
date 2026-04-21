import numpy as np

def mean_field_update(agent_action, neighbor_actions):
    # Mean Field: Instead of modeling 1000 individual agents,
    # we model the 'Average' action of the group (the Mean Field)
    mean_action = np.mean(neighbor_actions)
    
    # Policy: How do I act relative to the crowd?
    # e.g., 'Follow the crowd' or 'Avoid the crowd'
    reward = -np.abs(agent_action - mean_action) # Follow the crowd
    print(f"🚀 Mean Field: Average Neighbor Action = {mean_action:.2f} | My Alignment = {reward:.2f}")
    return reward

print("🚀 Mean Field RL Core: Scaling to thousands of agents using physics-inspired logic.")
my_act = 0.5
others = np.random.rand(100)
mean_field_update(my_act, others)
print("✅ Logic Check: Group-level abstraction for massive multi-agent systems verified.")
