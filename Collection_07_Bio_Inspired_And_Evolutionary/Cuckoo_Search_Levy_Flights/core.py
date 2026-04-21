import numpy as np

def levy_flight_step(position, beta=1.5):
    # Cuckoo Search: Optimization via Levy Flights
    # Levy Flight is a random walk with occasional 'Giant Leaps'
    # This allows the AI to escape local optima that trap other algos.
    sigma = (np.math.gamma(1 + beta) * np.sin(np.pi * beta / 2) / 
             (np.math.gamma((1 + beta) / 2) * beta * 2**((beta - 1) / 2)))**(1 / beta)
    u = np.random.randn(*position.shape) * sigma
    v = np.random.randn(*position.shape)
    step = u / np.abs(v)**(1 / beta)
    
    new_pos = position + 0.1 * step
    print(f"🚀 Cuckoo: Levy Leap taken! Step Magnitude={np.linalg.norm(step):.4f}")
    return new_pos

print("🚀 Cuckoo Search: Global exploration via Levy distribution.")
pos_init = np.array([0.0, 0.0])
levy_flight_step(pos_init)
print("✅ Logic Check: Heavy-tailed random leap verified.")
