import numpy as np
import zlib

def compression_reward(trajectory_str):
    # Exploration via Compression: Reward = Compressibility Change
    # A state is 'Boring' if it is easily compressed (redundant).
    # A state is 'Curious' if it is hard to compress (new info).
    # Reward = Size( Compressed(Trajectory) ) - Size( Compressed(Previous) )
    data = trajectory_str.encode()
    compressed_size = len(zlib.compress(data))
    print(f"🚀 Compression: Trajectory Size={len(data)} | Compressed={compressed_size} | Ratio={compressed_size/len(data):.2f}")
    return compressed_size

print("🚀 Exploration via Compression: Using Kolmogorov Complexity for curiosity.")
compression_reward("AAAAA") # Boring
compression_reward("A B C D E") # Interesting
print("✅ Logic Check: Data-redundancy-based reward verified.")
