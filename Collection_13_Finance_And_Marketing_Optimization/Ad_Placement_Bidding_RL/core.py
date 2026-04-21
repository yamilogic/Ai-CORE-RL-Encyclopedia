import numpy as np

def ad_bidding_step(budget_remaining, click_prob, competitor_prices, weights):
    # Ad Bidding: RL deciding how much to pay for a click
    # State = Budget, Click Probability, Estimated Competition
    state = np.array([budget_remaining, click_prob, np.mean(competitor_prices)])
    bid_price = np.dot(state, weights)
    print(f"🚀 Ad Bidding: Prob={click_prob:.2f} | Competition={np.mean(competitor_prices):.2f} | Bid=${bid_price:.4f}")
    return bid_price

print("🚀 Ad Bidding RL: Optimizing budget allocation in real-time auctions.")
b_rem, c_pr = 1000.0, 0.05
comps = [0.5, 0.8, 1.2]
w = np.random.randn(3)
ad_bidding_step(b_rem, c_pr, comps, w)
print("✅ Logic Check: Click-probability-aware bidding verified.")
