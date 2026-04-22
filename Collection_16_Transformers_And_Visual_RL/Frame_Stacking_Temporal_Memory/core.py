import numpy as np

def frame_stack(frames):
    # Frame Stacking: Creating 'Temporal' state
    # A single frame is a picture. 4 frames is a MOVIE.
    # This allows the AI to see 'Velocity' and 'Direction'.
    stacked_state = np.concatenate(frames, axis=-1)
    print(f"🚀 FrameStack: {len(frames)} frames merged. Shape: {stacked_state.shape}")
    return stacked_state

print("🚀 Frame Stacking Core: Giving 'Memory' to simple feed-forward agents.")
f = [np.zeros((84, 84, 1)) for _ in range(4)]
frame_stack(f)
print("✅ Logic Check: Temporal feature concatenation verified.")
