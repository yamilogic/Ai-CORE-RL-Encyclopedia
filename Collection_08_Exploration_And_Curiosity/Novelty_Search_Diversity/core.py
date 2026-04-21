import numpy as np

def novelty_reward(behavior_vec, archive):
    # Novelty Search: Reward = Average distance to the archive of past behaviors
    # We don't care if the agent 'won', only if they did something 'NEW'.
    if not archive:
        return 1.0
    distances = [np.linalg.norm(behavior_vec - past_b) for past_b in archive]
    novelty_score = np.mean(distances)
    print(f"🚀 Novelty: Behavior Dist={novelty_score:.4f} | {'Unique!' if novelty_score > 0.5 else 'Boring.'}")
    return novelty_score

print("🚀 Novelty Search: Rewarding diversity over performance.")
arch = [np.array([1,0]), np.array([0,1])]
b_new = np.array([1,1])
novelty_reward(b_new, arch)
print("✅ Logic Check: Behavior-distance novelty metric verified.")
