from datetime import datetime, timezone
import json
from app.core.config import redis_client
from app.services.users_service import get_following
from typing import List
from app.core.test_config import test_redis_client


redis = test_redis_client if "pytest" in globals() else redis_client

def get_timeline(user_id: str, page: int = 1, page_size: int = 10) -> List[dict]:

    following = get_following(user_id)  
    timeline = []

    for follow_id in following:
        key = f"user:{follow_id}:tweets"
        tweets = redis.lrange(key, 0, -1)  
        for tweet in tweets:
            if not tweet:
                continue
            try:
                tweet_data = json.loads(tweet)  
                tweet_data["user_id"] = follow_id
                timeline.append(tweet_data)
            except json.JSONDecodeError:
                print(f"Error decoding tweet from {follow_id}: {tweet}")
                continue

    timeline.sort(key=lambda x: datetime.strptime(x["timestamp"], '%Y-%m-%d %H:%M'), reverse=True)

    start = (page - 1) * page_size
    end = start + page_size
    return timeline[start:end]
