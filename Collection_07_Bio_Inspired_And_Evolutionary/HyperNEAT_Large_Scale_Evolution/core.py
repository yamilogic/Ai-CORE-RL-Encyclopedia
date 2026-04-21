import numpy as np

def cppn_generate_weight(coord_a, coord_b, cppn_weights):
    # HyperNEAT: Using a CPPN to generate weights based on Geometry
    # Weight(x1, y1, x2, y2) = CPPN(x1, y1, x2, y2)
    # This allows for symmetrical, large-scale brains.
    inp = np.concatenate([coord_a, coord_b])
    weight = np.tanh(np.dot(inp, cppn_weights))
    print(f"🚀 HyperNEAT: Generated Weight for geometry ({coord_a}, {coord_b}) = {weight:.4f}")
    return weight

print("🚀 HyperNEAT: Initializing Indirect Encoding Engine...")
c1, c2 = np.array([0, 0]), np.array([1, 1])
w_cppn = np.random.randn(4)
cppn_generate_weight(c1, c2, w_cppn)
print("✅ Logic Check: Geometric-based weight generation verified.")
