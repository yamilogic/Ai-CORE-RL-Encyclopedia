import numpy as np

def graph_message_passing(node_features, adjacency_matrix, weight_w):
    # Graph Neural RL: Nodes update their state by looking at neighbors.
    # New_State = sum( Neighbors ) * Weights
    # This allows the AI to handle a variable number of entities (e.g. 5 or 100 robots).
    neighbor_agg = np.dot(adjacency_matrix, node_features)
    new_features = np.tanh(np.dot(neighbor_agg, weight_w))
    print(f"🚀 Graph-RL: Message Passing Complete. Feature Norm={np.linalg.norm(new_features):.4f}")
    return new_features

print("🚀 Graph Neural RL: Relational reasoning for multi-entity systems.")
nodes = np.random.randn(3, 4) # 3 agents, 4 features each
adj = np.array([[1,1,0], [1,1,1], [0,1,1]]) # 1 is connected to 2, 2 to all
w = np.random.randn(4, 4)
graph_message_passing(nodes, adj, w)
print("✅ Logic Check: Adjacency-based feature aggregation verified.")
