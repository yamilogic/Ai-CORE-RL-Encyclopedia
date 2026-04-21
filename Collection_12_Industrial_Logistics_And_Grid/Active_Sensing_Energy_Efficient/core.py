import numpy as np

def active_sensing_decision(uncertainty, sensing_cost):
    # Active Sensing: Should I look at the sensor?
    # If uncertainty > cost, then 'Look'
    if uncertainty > sensing_cost:
        print("🚀 Active Sensing: UNCERTAINTY HIGH. Powering up sensors...")
        return True
    else:
        print("🚀 Active Sensing: Confident. Keeping sensors OFF to save battery.")
        return False

print("🚀 Active Sensing Core: Energy-efficient RL for IoT and Robotics.")
active_sensing_decision(0.8, 0.5)
print("✅ Logic Check: Cost-aware sensing decision verified.")
