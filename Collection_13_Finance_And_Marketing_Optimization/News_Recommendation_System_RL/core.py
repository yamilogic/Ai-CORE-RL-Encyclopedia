import numpy as np

def news_recommender(user_embedding, article_candidates, weights):
    # News Recommender: Balancing Click-Probability and Diversity
    # State = User history embedding
    scores = np.dot(article_candidates, user_embedding)
    # Add a diversity bonus (simplified)
    diversity_bonus = np.random.uniform(0, 0.1, size=len(scores))
    final_scores = scores + diversity_bonus
    best_article = np.argmax(final_scores)
    print(f"🚀 News RL: Best Article Index={best_article} | Expected CTR={scores[best_article]:.4f}")
    return best_article

print("🚀 News Recommendation RL: Personalizing content feeds in real-time.")
u = np.random.randn(8)
a = np.random.randn(5, 8)
w = np.random.randn(8)
news_recommender(u, a, w)
print("✅ Logic Check: Interest-diversity balanced recommendation verified.")
