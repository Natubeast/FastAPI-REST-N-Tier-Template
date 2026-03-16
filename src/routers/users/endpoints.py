from fastapi import Depends, HTTPException
from pydantic import BaseModel
from typing import List
from src.services.user_service import UserService

class UserCreate(BaseModel):
    name: str
    email: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

async def create_user(user: UserCreate, service: UserService = Depends(UserService)):
    return await service.create_user(user.name, user.email)

async def get_users(service: UserService = Depends(UserService)):
    return await service.get_users()

async def get_user(user_id: int, service: UserService = Depends(UserService)):
    user = await service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user