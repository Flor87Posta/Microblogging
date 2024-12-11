from fastapi import FastAPI
from app.api.v1.endpoints import tweets, users, timeline
from app.core.config import redis_client

app = FastAPI()

@app.get("/")
async def root():
    redis_client.set("test_key", "Hello, Redis!")
    return {"message": redis_client.get("test_key")}

app.include_router(tweets.router, prefix="/api/v1")
app.include_router(users.router, prefix="/api/v1")
app.include_router(timeline.router, prefix="/api/v1")