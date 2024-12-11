from fastapi import APIRouter, HTTPException
from app.schemas.tweet import TweetCreate
from app.services.tweets_service import publish_tweet, get_tweets

router = APIRouter()

@router.post("/tweets", status_code=201)
async def create_tweet(tweet: TweetCreate):
    try:
        publish_tweet(tweet.user_id, tweet.content)
        return {"message": "Tweet published successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error publishing tweet: {e}")

@router.get("/tweets/{user_id}")
async def read_tweets(user_id: str):
    try:
        tweets = get_tweets(user_id)
        if not tweets:
            return {"message": "No tweets found for this user"}
        return {"user_id": user_id, "tweets": tweets}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching tweets: {e}")