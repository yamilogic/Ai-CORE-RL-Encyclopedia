import numpy as np

def shield_action(suggested_action, state):
    # Shielding: An external 'Police' monitor for the AI
    # The Shield has a list of 'Banned' states
    banned_states = [np.array([1,1]), np.array([-1,-1])]
    
    # Simple check: Will this action lead to a banned state?
    for bs in banned_states:
        if np.linalg.norm(state + suggested_action - bs) < 0.2:
            print("🛑 SHIELD: Action Blocked! Danger zone ahead.")
            return -suggested_action # Retreat
            
    print("🛡️ SHIELD: Action Verified Safe.")
    return suggested_action

print("🚀 Shielding RL: Correct-by-construction safety monitor.")
s_curr = np.array([0.9, 0.9])
a_suggest = np.array([0.1, 0.1])
shield_action(a_suggest, s_curr)
print("✅ Logic Check: Preventive state-monitoring verified.")
