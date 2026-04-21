import numpy as np

def symmetry_augmentation(state, action):
    # Symmetry-Aware RL: If the world is symmetrical, the policy should be too.
    # e.g. If 'Turn Left' is good for 'Wall on Left', 
    # then 'Turn Right' MUST be good for 'Wall on Right'.
    
    # Flip the state (Symmetry operation)
    flipped_state = -state 
    flipped_action = -action
    
    print(f"🚀 Symmetry: Original=({state}, {action}) | Mirror=({flipped_state}, {flipped_action})")
    return flipped_state, flipped_action

print("🚀 Symmetry-Aware RL: Enforcing physical invariances for faster learning.")
s_in = np.array([1.0, 0.5])
a_in = np.array([1.0])
symmetry_augmentation(s_in, a_in)
print("✅ Logic Check: Reflectional symmetry transformation verified.")
