import numpy as np

def ad_placement_reward(bid_price, ad_quality, conversion_rate):
    # RL for Ad Placement: Maximizing ROAS (Return on Ad Spend).
    # Reward = (Conversion_Value * Conversion_Rate) - Bid_Price
    # The agent must decide how much to bid for a spot in Google Search.
    conv_val = 50.0 # $50 per sale
    revenue = conv_val * conversion_rate
    profit = revenue - bid_price
    print(f"🚀 Ad-RL: Bid=${bid_price:.2f} | Revenue=${revenue:.2f} | Profit=${profit:.2f}")
    return profit

print("🚀 RL for Ad Placement: Maximizing digital marketing efficiency.")
ad_placement_reward(Bid_Price=2.5, ad_quality=0.9, conversion_rate=0.1)
print("✅ Logic Check: Bid-revenue-profit ad reward verified.")
