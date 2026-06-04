from fastapi import APIRouter, Depends
from app.core.security import get_current_user

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("/me")
def get_my_tasks(user=Depends(get_current_user)):
    return {
        "message": "Protected route working",
        "user": user.email
    }