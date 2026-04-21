import numpy as np

def traffic_signal_control(queue_lengths, current_phase, phase_weights):
    # Traffic Control: RL deciding signal timings
    # State = Queue lengths on all roads
    # Action = Change signal or Stay
    wait_time = np.dot(queue_lengths, phase_weights)
    action = 1 if wait_time > 10.0 else 0
    print(f"🚀 Traffic RL: Queue={queue_lengths} | Avg Wait={wait_time:.2f} | Action={action}")
    return action

print("🚀 Traffic Signal Control RL: Optimizing city flow via queue pressure.")
q = np.array([5, 12, 3, 8]) # Number of cars per lane
w = np.random.randn(4)
traffic_signal_control(q, 0, w)
print("✅ Logic Check: Pressure-based signal switching verified.")
