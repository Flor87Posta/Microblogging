from datetime import datetime, timezone
import json
from app.core.config import redis_client
from app.core.test_config import test_redis_client

redis = test_redis_client if "pytest" in globals() else redis_client

def save_tweet(tweet_id: str, tweet_content: str):
    redis.set(tweet_id, tweet_content)

def get_tweets(user_id: str) -> list:
    key = f"user:{user_id}:tweets"
    tweets = redis.lrange(key, 0, -1)
    return [json.loads(tweet) for tweet in tweets]

def publish_tweet(user_id: str, content: str) -> None:
    key = f"user:{user_id}:tweets"
    timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M')
    tweet_data = {"content": content, "timestamp": timestamp}
    redis.rpush(key, json.dumps(tweet_data))
