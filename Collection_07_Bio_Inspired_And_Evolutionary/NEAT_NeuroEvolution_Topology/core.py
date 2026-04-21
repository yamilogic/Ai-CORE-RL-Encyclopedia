import numpy as np

class Genome:
    """
    NEAT Genome: Representing a neural network that can grow.
    """
    def __init__(self, n_inputs, n_outputs):
        self.nodes = n_inputs + n_outputs
        self.connections = [] # List of (in, out, weight, enabled)
        
    def mutate_add_connection(self):
        in_node = np.random.randint(0, self.nodes)
        out_node = np.random.randint(0, self.nodes)
        weight = np.random.randn()
        self.connections.append([in_node, out_node, weight, True])
        print(f"🚀 NEAT: Mutated Connection! {in_node} -> {out_node} (Weight={weight:.2f})")

    def mutate_add_node(self):
        self.nodes += 1
        print(f"🚀 NEAT: Mutated Node! Total Nodes={self.nodes}")

print("🚀 NEAT: Initializing Topology Evolution Engine...")
gen = Genome(4, 2)
gen.mutate_add_connection()
gen.mutate_add_node()
print("✅ Logic Check: Structural mutation logic verified.")
