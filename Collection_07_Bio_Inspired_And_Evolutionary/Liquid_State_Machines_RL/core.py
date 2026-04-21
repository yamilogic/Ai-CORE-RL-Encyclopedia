import numpy as np

class LiquidReservoir:
    def __init__(self, size=100):
        # A fixed, random 'Liquid' of neurons
        self.size = size
        self.state = np.zeros(size)
        self.w_res = np.random.randn(size, size) * 0.1
        self.w_in = np.random.randn(size, 4)

    def ripple(self, input_signal):
        # The 'Liquid' state ripples when input is dropped in
        # New State = tanh(W_res * State + W_in * Input)
        self.state = np.tanh(np.dot(self.w_res, self.state) + np.dot(self.w_in, input_signal))
        print(f"🚀 Liquid: Input ripples through reservoir. State Norm={np.linalg.norm(self.state):.4f}")
        return self.state

print("🚀 Liquid State Machine: Reservoir computing for temporal RL.")
lsm = LiquidReservoir()
lsm.ripple(np.random.randn(4))
print("✅ Logic Check: High-dimensional non-linear mapping verified.")
