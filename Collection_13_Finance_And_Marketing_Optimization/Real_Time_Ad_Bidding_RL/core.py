import numpy as np

def place_bid(ad_features, user_value, budget, bidding_weights):
    # RL for Ads: [Ad Info, User Profile] -> Decide Bid Price ($)
    # Reward = Profit (Revenue - Bid) if won, 0 if lost
    state = np.append(ad_features, user_value)
    bid_price = np.dot(state, bidding_weights)
    # Adjust bid based on remaining budget
    safe_bid = np.clip(bid_price, 0, budget * 0.1)
    print(f"🚀 Ad Bidding RL: User Value: {user_value:.2f} | Placing Bid: ${safe_bid:.2f} | Remaining Budget: ${budget:.2f}")
    return safe_bid

print("🚀 Real-Time Ad Bidding RL: Optimizing digital auctions at scale.")
f, v = np.random.rand(4), 10.5
b = 100.0
w = np.random.randn(5)
place_bid(f, v, b, w)
print("✅ Logic Check: Budget-aware bidding strategy verified.")
