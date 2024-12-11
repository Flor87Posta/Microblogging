from pydantic import BaseModel, Field

class TweetCreate(BaseModel):
    user_id: str = Field(..., description="ID of the user creating the tweet")
    content: str = Field(..., max_length=280, description="Content of the tweet (max 280 characters)")
