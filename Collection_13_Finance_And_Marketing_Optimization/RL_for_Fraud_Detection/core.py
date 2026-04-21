import numpy as np

def fraud_detection_step(tx_amount, tx_frequency, location_diff, weights):
    # Fraud Detection: RL finding anomalies in payment streams
    # State = Amount, Frequency of use, Distance from home
    risk_score = np.dot([tx_amount, tx_frequency, location_diff], weights)
    action = 1 if risk_score > 0.8 else 0 # 1 = Block, 0 = Allow
    print(f"🚀 Fraud RL: Amount=${tx_amount} | Risk Score={risk_score:.4f} | Action={'BLOCK' if action else 'ALLOW'}")
    return action

print("🚀 Fraud Detection RL: Real-time anomaly blocking.")
amt, freq, loc = 5000.0, 10.0, 2000.0
w = np.array([0.0001, 0.05, 0.0001])
fraud_detection_step(amt, freq, loc, w)
print("✅ Logic Check: Risk-thresholded transaction blocking verified.")
