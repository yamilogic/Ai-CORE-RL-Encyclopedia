import numpy as np

def noisy_layer(x, w, b, sigma_w, sigma_b):
    # Add random noise directly to the weights
    epsilon_w = np.random.randn(*w.shape)
    epsilon_b = np.random.randn(*b.shape)
    
    noisy_w = w + sigma_w * epsilon_w
    noisy_b = b + sigma_b * epsilon_b
    
    return np.dot(x, noisy_w) + noisy_b

print("🚀 Noisy Networks: Exploration through Parameter Noise (No Epsilon needed).")
x = np.random.randn(4)
w, b = np.random.randn(4, 2), np.random.randn(2)
out = noisy_layer(x, w, b, 0.1, 0.1)
print(f"✅ Noisy Output: {out} | Exploring via weight randomness.")
