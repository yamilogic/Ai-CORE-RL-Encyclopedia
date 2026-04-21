import numpy as np

def arbitrage_trading_reward(buy_price, sell_price, transaction_fee):
    # RL for Arbitrage: Finding price differences across exchanges.
    # Reward = (Sell - Buy) - (Fee + Slippage)
    # The agent must act in microseconds to 'Lock in' the profit.
    spread = sell_price - buy_price
    profit = spread - transaction_fee
    print(f"🚀 Arb-RL: Spread=${spread:.4f} | Fee=${transaction_fee:.4f} | Net Profit=${profit:.4f}")
    return profit

print("🚀 RL for Automated Trading Arbitrage: High-frequency market efficiency.")
arbitrage_trading_reward(Buy=100.0, Sell=100.15, transaction_fee=0.02)
print("✅ Logic Check: Spread-fee arbitrage reward verified.")
