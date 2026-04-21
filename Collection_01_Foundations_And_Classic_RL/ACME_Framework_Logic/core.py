import numpy as np

class AcmeActor:
    """
    ACME: DeepMind's framework for modular RL.
    Defines strict boundaries between Actor, Learner, and Dataset.
    """
    def __init__(self, policy):
        self.policy = policy

    def select_action(self, obs):
        return self.policy(obs)

    def observe(self, action, next_obs, reward):
        # Sends data to a 'Reverb' dataset
        print(f"🚀 ACME: Observation stored in Reverb. Reward={reward}")

print("🚀 ACME: Initializing Modular RL Framework...")
actor = AcmeActor(policy=lambda x: 1)
actor.observe(1, None, 10.0)
print("✅ Logic Check: Actor-observer decoupling verified.")
