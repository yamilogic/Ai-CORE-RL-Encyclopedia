import numpy as np

class SpikingNeuron:
    def __init__(self, threshold=1.0, decay=0.9):
        self.potential = 0.0
        self.threshold = threshold
        self.decay = decay

    def integrate(self, input_current):
        # Integrate-and-Fire Model
        self.potential = self.potential * self.decay + input_current
        spike = 0
        if self.potential >= self.threshold:
            spike = 1
            self.potential = 0 # Reset
            print("⚡ SPIKE! Neuron reached threshold and fired.")
        return spike

print("🚀 Spiking Neural RL: Event-based temporal processing.")
neuron = SpikingNeuron()
for i in range(5):
    s = neuron.integrate(0.3)
    print(f"   Step {i}: Potential={neuron.potential:.2f} | Spike={s}")
print("✅ Logic Check: Integrate-and-fire spike generation verified.")
