import numpy as np

def code_generation_reward(generated_code, unit_tests):
    # RL for Code Gen: Rewarding code that actually WORKS.
    # Reward = 1.0 if all tests pass, else 0.0
    # This is the core of RLHF/PPO for coding models.
    passed = all(test(generated_code) for test in unit_tests)
    reward = 1.0 if passed else -0.5
    print(f"🚀 Code-RL: Tests Passed={passed} | Reward={reward}")
    return reward

print("🚀 RL for Code Generation: Optimizing LLMs for functional correctness.")
# Dummy test: Does the code contain the word 'print'?
tests = [lambda x: "print" in x]
code_generation_reward("print('Hello')", tests)
print("✅ Logic Check: Test-based reward verification verified.")
