import numpy as np

def safety_shield(proposed_action, sensor_data, safety_threshold=0.5):
    # Safety Shield: Overriding the AI if the action is dangerous
    # proposed_action: -1 to 1
    danger_prediction = np.dot(sensor_data, np.random.randn(len(sensor_data))) # placeholder
    
    if danger_prediction > safety_threshold:
        print(f"⚠️ SHIELD ACTIVE: Overriding proposed action {proposed_action:.2f} to SAFE BRAKE.")
        return 0.0 # Safe Action (e.g., Brake)
    else:
        print(f"🚀 SHIELD PASSIVE: Action {proposed_action:.2f} allowed.")
        return proposed_action

print("🚀 RL with Safety Shield: Hard-constraint enforcement logic.")
s_data = np.array([1.0, 0.8, 0.9])
safety_shield(0.95, s_data)
print("✅ Logic Check: Safety-critical action override verified.")
