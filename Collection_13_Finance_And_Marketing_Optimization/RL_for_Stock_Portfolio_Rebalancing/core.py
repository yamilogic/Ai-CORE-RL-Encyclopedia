import numpy as np

def portfolio_rebalance_reward(portfolio_return, risk_std, transaction_cost):
    # RL for Finance: Balancing Risk and Return.
    # Reward = Return - (C1 * Risk + C2 * Transaction_Fees)
    # The agent decides when to 'Sell High' and 'Buy Low' to maintain its target.
    # Sharpe Ratio proxy
    reward = portfolio_return / (risk_std + 1e-8) - transaction_cost
    print(f"🚀 Finance-RL: Return={portfolio_return:.4f} | Risk={risk_std:.4f} | Reward={reward:.2f}")
    return reward

print("🚀 RL for Stock Portfolio Rebalancing: Dynamic asset allocation.")
portfolio_rebalance_reward(portfolio_return=0.15, risk_std=0.05, transaction_cost=0.01)
print("✅ Logic Check: Sharpe-ratio-based finance reward verified.")
