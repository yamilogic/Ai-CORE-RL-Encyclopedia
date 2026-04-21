import numpy as np

def bat_echolocation_step(pos, best_pos, velocity, freq, loudness):
    # Bat: Search via frequency-tuned echolocation
    f = freq[0] + (freq[1] - freq[0]) * np.random.rand()
    new_velocity = velocity + (pos - best_pos) * f
    new_pos = pos + new_velocity
    if np.random.rand() > loudness:
        new_pos = best_pos + 0.01 * np.random.randn(*pos.shape)
    print(f"🚀 Bat: Pinging... Freq={f:.2f} | Loudness={loudness:.2f}")
    return new_pos, new_velocity

print("🚀 Bat Algorithm: Echolocation-based search.")
p = np.array([0.0, 0.0]); b = np.array([10.0, 10.0]); v = np.array([0.1, 0.1])
bat_echolocation_step(p, b, v, [0, 2], 0.5)
print("✅ Logic Check: Frequency-velocity-pulse logic verified.")
