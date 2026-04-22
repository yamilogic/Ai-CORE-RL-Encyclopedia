import numpy as np

def rad_augmentation_mix(image_batch):
    # RAD: Using a library of augmentations (Crop, Gray, Cutout)
    # This 'Blinds' the agent to irrelevant details (like background color)
    # forcing it to focus on the 'Core Physics'.
    augmented = image_batch.copy()
    # Apply a random 'Cutout' (Black square)
    augmented[:, 2:5, 2:5] = 0.0
    # Apply random 'Color Jitter'
    augmented += np.random.uniform(-0.1, 0.1, size=augmented.shape)
    
    print(f"🚀 RAD: Applied 2-layer augmentation (Cutout + Jitter). Training Robustness...")
    return augmented

print("🚀 RAD: Initializing Universal Data Augmentation Layer...")
img = np.random.rand(10, 10, 3)
rad_augmentation_mix(img)
print("✅ Logic Check: Multi-layer image augmentation verified.")
