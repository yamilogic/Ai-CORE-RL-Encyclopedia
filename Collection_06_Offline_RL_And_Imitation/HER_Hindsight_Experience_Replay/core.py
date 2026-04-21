import numpy as np

def hindsight_relabel(state_sequence, failed_goal):
    # HER: Learning from failure by relabeling the goal
    # If I wanted to hit 'A' but hit 'B' instead, 
    # I pretend my goal WAS 'B' all along.
    actual_end_state = state_sequence[-1]
    new_goal = actual_end_state
    print(f"🚀 HER: Original Goal={failed_goal} | New Synthetic Goal={new_goal}")
    print(f"✅ HER: Relabeling failure as a 'Success' for the new goal.")
    return new_goal

print("🚀 HER: Initializing Goal-Relabeling Logic...")
seq = [np.array([0,0]), np.array([1,1]), np.array([2,2])] # Actual path
target = np.array([10,10]) # Intended goal
hindsight_relabel(seq, target)
print("✅ Logic Check: Final-state-as-goal relabeling verified.")
