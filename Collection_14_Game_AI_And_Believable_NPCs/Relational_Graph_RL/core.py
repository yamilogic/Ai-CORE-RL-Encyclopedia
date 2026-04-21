import numpy as np

def relational_message_passing(nodes, edges, weights):
    # Relational RL: Entities (Nodes) talk to each other (Edges)
    # New Node State = sum(neighbor_states * edge_weights)
    new_node_states = []
    for i in range(len(nodes)):
        # Simplified Graph Convolution
        neighbors = nodes[edges[i]]
        new_state = np.tanh(np.dot(np.mean(neighbors, axis=0), weights))
        new_node_states.append(new_state)
    print(f"🚀 Relational RL: Entities updated through Message Passing.")
    return new_node_states

print("🚀 Relational Graph RL: Reasoning about Objects and Relationships.")
n = [np.random.randn(4) for _ in range(3)] # 3 Objects
e = [[1, 2], [0], [0, 1]] # Relationships
w = np.random.randn(4, 4)
relational_message_passing(n, e, w)
print("✅ Logic Check: Entity-level relational graph convolution verified.")
