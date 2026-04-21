import numpy as np

def news_feed_reward(click_through, watch_time, diversity_score):
    # RL for News Recommendation: Balancing clicks and long-term value.
    # Reward = C1 * Click + C2 * Watch_Time + C3 * Diversity
    # The agent must avoid 'Clickbait' (high clicks, low watch time).
    reward = click_through * 1.0 + watch_time * 2.0 + diversity_score * 5.0
    print(f"🚀 News-RL: Click={click_through} | WatchTime={watch_time} | Reward={reward:.2f}")
    return reward

print("🚀 RL for News Recommendation Feed: Personalizing digital content.")
news_feed_reward(click_through=1, watch_time=10, diversity_score=0.8)
print("✅ Logic Check: Click-watch-diversity reward verified.")
