from src.repositories.user_repository import UserRepository, UserCreate, UserResponse
from pydantic import BaseModel
from typing import List, Optional
from fastapi import Depends

class UserService:
    def __init__(self, repository: UserRepository = Depends(UserRepository)):
        self.repository = repository

    async def create_user(self, name: str, email: str) -> UserResponse:
        user = UserCreate(name=name, email=email)
        return self.repository.create_user(user)

    async def get_users(self) -> List[UserResponse]:
        return self.repository.get_users()

    async def get_user_by_id(self, user_id: int) -> Optional[UserResponse]:
        return self.repository.get_user_by_id(user_id)