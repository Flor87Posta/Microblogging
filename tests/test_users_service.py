import pytest
from app.services.users_service import follow_user, get_following
from app.core.config import redis_client
from app.core.test_config import test_redis_client

@pytest.fixture(autouse=True)
def clean_redis():
    print("Limpieza inicial de Redis...")
    test_redis_client.flushall()
    keys = test_redis_client.keys("*")
    assert len(keys) == 0, f"Redis aún contiene claves: {keys}"


def test_follow_user():
    user_id = "test_user"
    follow_id = "follow_user"
    follow_user(user_id, follow_id)
    following = get_following(user_id)
    assert len(following) == 1
    assert following[0] == follow_id

def test_get_following():
    user_id = "test_user"
    follow_user(user_id, "follow_user_1")
    follow_user(user_id, "follow_user_2")
    following = get_following(user_id)
    assert len(following) == 2
    assert "follow_user_1" in following
    assert "follow_user_2" in following
