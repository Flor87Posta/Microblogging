import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.core.test_config import test_redis_client
from app.services.tweets_service import publish_tweet, get_tweets

client = TestClient(app)

@pytest.fixture(autouse=True)
def clean_redis():
    print("Limpieza inicial de Redis...")
    test_redis_client.flushall()
    keys = test_redis_client.keys("*")
    assert len(keys) == 0, f"Redis aún contiene claves: {keys}"

def test_publish_tweet():
    user_id = "test_user"
    content = "This is a test tweet"
    publish_tweet(user_id, content)
    tweets = get_tweets(user_id)

    assert len(tweets) == 1
    assert tweets[0]["content"] == content

    keys = test_redis_client.keys("*")
    print(f"Claves en Redis: {keys}")

def test_tweet_max_length():
    response = client.post(
        "/api/v1/tweets",
        json={
            "user_id": "test_user",
            "content": "A" * 281
        }
    )
    assert response.status_code == 422
    # Verificar el mensaje actualizado
    assert "String should have at most 280 characters" in response.text

