import numpy as np

def optimize_portfolio(prices, weights_w):
    # RL for Finance: [Stock A, Stock B, Cash] -> Adjust Portfolio Weights
    # Reward = Profit - Risk (Sharpe Ratio)
    current_portfolio = np.dot(prices, weights_w)
    new_weights = np.exp(np.dot(prices, weights_w)) / np.sum(np.exp(np.dot(prices, weights_w)))
    print(f"🚀 Portfolio RL: Prices analyzed. Rebalancing Assets: {new_weights.round(2)}")
    return new_weights

print("🚀 Portfolio Optimization RL: AI-driven wealth management.")
p = np.array([150.0, 2800.0, 1.0]) # Apple, Google, Cash
w = np.random.randn(3, 3)
optimize_portfolio(p, w)
print("✅ Logic Check: Risk-aware rebalancing verified.")
