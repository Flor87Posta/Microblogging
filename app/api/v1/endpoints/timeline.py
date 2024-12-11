from fastapi import APIRouter, HTTPException, Query  
from app.services.timeline_service import get_timeline

router = APIRouter()

@router.get("/users/{user_id}/timeline")
async def read_timeline(
    user_id: str,
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=50)
):
    try:
        timeline = get_timeline(user_id, page, page_size)
        if not timeline:
            return {"message": "No tweets found in the timeline"}
        return {"user_id": user_id, "timeline": timeline}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching timeline: {e}")