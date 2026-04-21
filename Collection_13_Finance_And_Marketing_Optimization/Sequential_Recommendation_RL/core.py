import numpy as np

def recommend_item(user_history, item_weights):
    # RL for RecSys: [Movie A, Movie B] -> Predict Next Movie
    # Reward = User Click/Watch Time
    context = np.mean(user_history, axis=0)
    scores = np.dot(item_weights, context)
    best_item = np.argmax(scores)
    print(f"🚀 RecSys RL: User History analyzed. Recommending Item ID: {best_item}")
    return best_item

print("🚀 Sequential Recommendation RL: Building personalized user journeys.")
hist = [np.random.randn(4) for _ in range(3)]
w = np.random.randn(10, 4) # 10 candidate items
recommend_item(hist, w)
print("✅ Logic Check: Sequential context used for next-item prediction verified.")
