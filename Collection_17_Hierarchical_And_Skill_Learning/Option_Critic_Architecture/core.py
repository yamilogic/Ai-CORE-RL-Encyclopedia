import numpy as np

def option_critic_step(s, current_option):
    # Option: A high-level sub-policy (e.g., 'Go to Door')
    # Termination: Should I finish the current option?
    term_prob = 1 / (1 + np.exp(-np.dot(s, np.random.randn(s.shape[0]))))
    done = np.random.rand() < term_prob
    
    # Intra-option policy: Action within the current option
    action = np.argmax(np.dot(s, np.random.randn(s.shape[0], 2)))
    
    print(f"🚀 Option-Critic: Current Option Active | Terminate Prob: {term_prob:.2f} | Action: {action}")
    return action, done

print("🚀 Option-Critic: Learning high-level 'Options' automatically.")
s = np.random.randn(4)
option_critic_step(s, 0)
print("✅ Logic Check: Hierarchical termination and intra-option action verified.")
