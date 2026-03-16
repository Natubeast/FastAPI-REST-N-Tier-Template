from fastapi import APIRouter
from .endpoints import create_user, get_users, get_user

router = APIRouter(prefix="/users", tags=["users"])

router.post("/")(create_user)
router.get("/")(get_users)
router.get("/{user_id}")(get_user)
