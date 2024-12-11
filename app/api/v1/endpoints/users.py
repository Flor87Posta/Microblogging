from fastapi import APIRouter, HTTPException
from app.services.users_service import follow_user, get_following

router = APIRouter()

@router.post("/users/{user_id}/follow/{follow_id}", status_code=201)
async def follow(user_id: str, follow_id: str):
    try:
        if user_id == follow_id:
            raise HTTPException(status_code=400, detail="You cannot follow yourself.")
        follow_user(user_id, follow_id)
        return {"message": f"User {user_id} is now following {follow_id}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error following user: {e}")

@router.get("/users/{user_id}/following")
async def get_following_list(user_id: str):
    try:
        following = get_following(user_id)
        return {"user_id": user_id, "following": following}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching following list: {e}")
