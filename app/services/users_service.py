from app.core.config import redis_client
from app.core.test_config import test_redis_client

redis = test_redis_client if "pytest" in globals() else redis_client

def follow_user(user_id: str, follow_id: str) -> None:
    key = f"user:{user_id}:following"
    if redis.lpos(key, follow_id) is None: 
        redis.rpush(key, follow_id)

def get_following(user_id: str) -> list:
    key = f"user:{user_id}:following"
    return redis.lrange(key, 0, -1)
