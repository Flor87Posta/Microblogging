import pytest
from app.services.tweets_service import publish_tweet
from app.services.users_service import follow_user
from app.services.timeline_service import get_timeline
from app.core.config import redis_client
from app.core.test_config import test_redis_client

@pytest.fixture(autouse=True)
def clean_redis():
    print("Limpieza inicial de Redis...")
    test_redis_client.flushall()
    keys = test_redis_client.keys("*")
    assert len(keys) == 0, f"Redis aún contiene claves: {keys}"


def test_get_timeline():
    user_id = "test_user"
    follow_user(user_id, "user_1")
    follow_user(user_id, "user_2")

    publish_tweet("user_1", "Tweet from user 1")
    publish_tweet("user_2", "Tweet from user 2")

    timeline = get_timeline(user_id)

    assert len(timeline) == 2
    assert any(tweet["content"] == "Tweet from user 1" for tweet in timeline)
    assert any(tweet["content"] == "Tweet from user 2" for tweet in timeline)

    keys = test_redis_client.keys("*")
    print(f"Claves en Redis: {keys}")


