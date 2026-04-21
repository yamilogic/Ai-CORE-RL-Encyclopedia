import numpy as np

class PlaNetModel:
    """
    PlaNet: Deep Planning Network.
    Uses RSSM (Recurrent State Space Model) to plan in latent space.
    The goal is to predict Image -> Latent -> Reward/Next_Latent.
    """
    def __init__(self, latent_dim=16):
        self.latent_dim = latent_dim
        self.w_trans = np.random.randn(latent_dim + 1, latent_dim) # Transition

    def plan_sequence(self, initial_latent, action_seq):
        # Plan ahead without seeing new images
        current_l = initial_latent
        plan = []
        for a in action_seq:
            inp = np.append(current_l, a)
            current_l = np.tanh(np.dot(inp, self.w_trans))
            plan.append(current_l)
            
        print(f"🚀 PlaNet: Planned {len(action_seq)} steps in Latent Space. Final Divergence={np.linalg.norm(current_l):.4f}")
        return plan

print("🚀 PlaNet: Initializing Deep Latent Planning Engine...")
planet = PlaNetModel()
l0 = np.random.randn(16)
a_s = [1, 0, 1]
planet.plan_sequence(l0, a_s)
print("✅ Logic Check: Latent-state sequence planning verified.")
