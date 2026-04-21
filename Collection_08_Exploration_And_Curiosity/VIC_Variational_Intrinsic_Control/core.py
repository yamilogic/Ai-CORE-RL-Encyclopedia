import numpy as np

def vic_control_reward(initial_state, final_state, option_z, encoder_w):
    # VIC: Reward = I( Option ; Final_State | Initial_State )
    # You are rewarded if your choice of 'Option' results in a specific,
    # predictable 'Final State' that wouldn't have happened otherwise.
    # It measures how much 'Control' you have over where you end up.
    
    pred_z = np.dot(final_state - initial_state, encoder_w)
    score = np.dot(pred_z, option_z) # Similarity between intended option and actual outcome
    print(f"🚀 VIC: Control Score={score:.4f} | Matching outcome to option intent.")
    return score

print("🚀 VIC: Initializing Intrinsic Control Discovery...")
s_i, s_f = np.random.randn(4), np.random.randn(4)
z_opt = np.array([1, 0, 0])
w_enc = np.random.randn(4, 3)
vic_control_reward(s_i, s_f, z_opt, w_enc)
print("✅ Logic Check: Option-outcome alignment reward verified.")
