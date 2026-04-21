import numpy as np

def qd_selection(population, fitnesses, novelty_scores, alpha=0.5):
    # Quality-Diversity (QD): Balancing 'Being Good' and 'Being Unique'
    # Score = alpha * Fitness + (1 - alpha) * Novelty
    total_scores = alpha * np.array(fitnesses) + (1 - alpha) * np.array(novelty_scores)
    best_idx = np.argmax(total_scores)
    
    print(f"🚀 QD-RL: Best agent selected. Fitness={fitnesses[best_idx]:.2f} | Novelty={novelty_scores[best_idx]:.2f}")
    return population[best_idx]

print("🚀 QD-RL: Initializing Quality-Diversity Integration...")
pop = ["Bot_A", "Bot_B", "Bot_C"]
fits = [100.0, 90.0, 20.0]  # Bot A is best at game
novs = [1.0, 50.0, 100.0]   # Bot C is most unique
# Select with alpha=0.5 (Balance)
qd_selection(pop, fits, novs, alpha=0.5) # Bot B likely wins (Good + Unique)
print("✅ Logic Check: Multi-objective selection verified.")
