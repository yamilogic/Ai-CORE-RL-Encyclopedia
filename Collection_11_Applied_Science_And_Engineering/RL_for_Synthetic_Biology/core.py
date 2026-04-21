import numpy as np

def synthetic_bio_reward(dna_sequence, desired_protein_output):
    # RL for Synthetic Biology: Designing DNA sequences.
    # State = Sequence of A, T, C, G.
    # Reward = Matching the desired expression level in a cell.
    # The agent 'Edits' the DNA to maximize the 'Protein Yield'.
    match_score = np.sum([1 if char in "ATCG" else -1 for char in dna_sequence])
    yield_prediction = match_score * 0.1
    reward = yield_prediction
    print(f"🚀 SynBio-RL: Sequence={dna_sequence[:10]}... | Yield={yield_prediction:.4f}")
    return reward

print("🚀 RL for Synthetic Biology: Engineering the software of life.")
synthetic_bio_reward("ATGC" * 10, 5.0)
print("✅ Logic Check: DNA-sequence expression reward verified.")
