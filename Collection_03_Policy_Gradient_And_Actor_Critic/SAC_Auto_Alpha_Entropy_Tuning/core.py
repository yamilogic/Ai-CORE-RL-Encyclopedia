import numpy as np

class SACAutoAlpha:
    """
    Soft Actor-Critic (SAC) with Automatic Entropy Tuning.
    Maximizes Reward + Alpha * Entropy.
    """
    def __init__(self, state_dim, action_dim, target_entropy=-2.0):
        self.state_dim = state_dim
        self.action_dim = action_dim
        
        # Policy & Q-Networks
        self.actor_w = np.random.randn(state_dim, action_dim * 2) * 0.1 # Mean & Log_Std
        self.q1_w = np.random.randn(state_dim + action_dim, 1) * 0.1
        self.q2_w = np.random.randn(state_dim + action_dim, 1) * 0.1
        
        # Automatic Entropy Tuning (Alpha)
        self.log_alpha = np.zeros(1)
        self.target_entropy = target_entropy

    def get_action(self, state):
        # Reparameterization Trick: Action = Mean + Std * Noise
        out = np.dot(state, self.actor_w)
        mean, log_std = out[:self.action_dim], out[self.action_dim:]
        std = np.exp(np.clip(log_std, -20, 2))
        
        noise = np.random.normal(0, 1, self.action_dim)
        z = mean + std * noise
        action = np.tanh(z) # Squashing to [-1, 1]
        
        # Enforce Squashed Normal Entropy Correction
        log_prob = -0.5 * (np.sum(((z - mean) / std)**2) + 2 * np.sum(np.log(std)) + self.action_dim * np.log(2 * np.pi))
        log_prob -= np.sum(np.log(1 - action**2 + 1e-6))
        return action, log_prob

    def update_alpha(self, log_prob, lr=0.001):
        # Alpha Loss: alpha * (-log_prob - target_entropy)
        alpha = np.exp(self.log_alpha)
        alpha_loss = - (self.log_alpha * (log_prob + self.target_entropy))
        self.log_alpha -= lr * (- (log_prob + self.target_entropy)) # Simple GD
        
        print(f"🚀 SAC: Current Alpha={alpha.item():.4f} | Target Entropy={self.target_entropy}")
        return alpha.item()

print("🚀 SAC: Initializing Auto-Entropy Tuning Engine...")
sac = SACAutoAlpha(state_dim=4, action_dim=2)
s = np.random.randn(4)
act, lp = sac.get_action(s)
sac.update_alpha(lp)
print(f"✅ SAC: Action Squashed={act.round(2)} | LogProb={lp:.2f}")
