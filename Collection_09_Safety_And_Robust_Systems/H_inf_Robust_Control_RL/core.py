import numpy as np

def h_infinity_check(gamma, l2_gain):
    # H-infinity: Minimizing the worst-case disturbance
    # System is H-inf stable if the L2-gain is less than Gamma
    if l2_gain < gamma:
        print(f"🚀 H-infinity: System is ROBUST. Gain {l2_gain:.4f} < {gamma}")
        return True
    else:
        print(f"⚠️ H-infinity: System VULNERABLE. Worst-case disturbance may cause crash.")
        return False

print("🚀 H-infinity Robust RL: Preparing for the absolute worst-case scenario.")
h_infinity_check(1.0, 0.85)
print("✅ Logic Check: Gain-based robustness verification complete.")
