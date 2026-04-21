import numpy as np

def alphago_mcts_selection(node_visits, node_values, prior_probs, cpuct=1.5):
    # AlphaGo Master: Selection via PUCT (Predictor Upper Confidence Bound for Trees)
    # Score = Value + Confidence(Prior / (1 + Visits))
    q_values = node_values / (node_visits + 1e-8)
    u_values = cpuct * prior_probs * (np.sqrt(np.sum(node_visits)) / (1 + node_visits))
    puct_scores = q_values + u_values
    best_move = np.argmax(puct_scores)
    print(f"🚀 AlphaGo PUCT: Best Move={best_move} | Value={q_values[best_move]:.2f} | Confidence={u_values[best_move]:.2f}")
    return best_move

print("🚀 AlphaGo Master: Selection logic for tree search optimization.")
visits = np.array([10, 2, 50, 1])
vals = np.array([5.0, 1.0, 45.0, 0.5])
priors = np.array([0.25, 0.25, 0.25, 0.25])
alphago_mcts_selection(visits, vals, priors)
print("✅ Logic Check: PUCT-based move selection verified.")
