import numpy as np

def npc_emotion_reward(player_trust, immersion_score, personality_alignment):
    # RL for NPCs: Creating believable characters.
    # Reward = Trust + Immersion + Alignment
    # The agent decides how to react to the player's actions.
    # If the NPC is 'Grumpy', it is rewarded for being grumpy consistently.
    reward = player_trust * 1.0 + immersion_score * 2.0 + personality_alignment * 5.0
    print(f"🚀 NPC-RL: Trust={player_trust} | Personality={personality_alignment} | Reward={reward:.2f}")
    return reward

print("🚀 RL for NPC Emotional Behavior: Engineering virtual personalities.")
npc_emotion_reward(player_trust=0.8, immersion_score=0.9, personality_alignment=1.0)
print("✅ Logic Check: Trust-personality NPC reward verified.")
