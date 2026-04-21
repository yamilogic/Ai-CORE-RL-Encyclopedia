import numpy as np

def her_relabel(state, action, final_outcome):
    # Standard: Did I reach the Goal? (Usually No)
    real_reward = -1.0 
    # Hindsight: "Pretend" the final outcome WAS the goal
    hindsight_goal = final_outcome
    hindsight_reward = 0.0 # Success!
    print(f"🚀 HER: Relabeling failure as a success for goal {hindsight_goal}")
    return hindsight_reward

print("🚀 HER Core: Learning from every mistake by changing the goal.")
her_relabel(None, None, [4,4])
print("✅ Logic Check: Failed attempts converted into successful lessons.")
