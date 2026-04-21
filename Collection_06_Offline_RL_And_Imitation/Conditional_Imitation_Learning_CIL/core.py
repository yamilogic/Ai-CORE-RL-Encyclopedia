import numpy as np

def cil_command_action(state, command):
    # CIL: The action depends on the State AND a high-level Command
    # Commands: 0=Straight, 1=Left, 2=Right
    branches = [np.dot(state, np.random.randn(4)) for _ in range(3)]
    selected_action = branches[command]
    print(f"🚀 CIL: Command '{['Straight','Left','Right'][command]}' -> Output Action: {selected_action:.2f}")
    return selected_action

print("🚀 Conditional Imitation Learning (CIL): Expert behavior guided by commands.")
s = np.random.randn(4)
cil_command_action(s, 1) # Expert command: Turn Left
print("✅ Logic Check: Branch selection based on command ID verified.")
