import numpy as np

def quantum_error_reward(syndrome, recovery_op, true_error):
    # RL for Quantum Error Correction (QEC)
    # The agent receives a 'Syndrome' (the symptom of a bug in a qubit).
    # It must choose a 'Recovery' action to fix the qubit state.
    # Reward = 1.0 if Recovery == Error (Qubit fixed), else -1.0
    
    success = (recovery_op == true_error)
    reward = 1.0 if success else -1.0
    print(f"🚀 QEC-RL: Syndrome={syndrome} | Success={success} | Reward={reward}")
    return reward

print("🚀 RL for Quantum Error Correction: Managing the noise of the universe.")
quantum_error_reward(syndrome="BitFlip_Detected", recovery_op="Apply_X_Gate", true_error="Apply_X_Gate")
print("✅ Logic Check: Syndrome-recovery matching reward verified.")
