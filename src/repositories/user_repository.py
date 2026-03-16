from pydantic import BaseModel
from typing import List, Optional

class UserCreate(BaseModel):
    name: str
    email: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

class UserRepository:
    def __init__(self):
        # Mock data store (to be replaced with SQLAlchemy later)
        self.users = [
            UserResponse(id=1, name="John Doe", email="john@example.com"),
            UserResponse(id=2, name="Jane Smith", email="jane@example.com")
        ]
        self.next_id = 3

    def create_user(self, user: UserCreate) -> UserResponse:
        new_user = UserResponse(id=self.next_id, name=user.name, email=user.email)
        self.users.append(new_user)
        self.next_id += 1
        return new_user

    def get_users(self) -> List[UserResponse]:
        return self.users

    def get_user_by_id(self, user_id: int) -> Optional[UserResponse]:
        for user in self.users:
            if user.id == user_id:
                return user
        return None
# This is a simple in-memory user repository.
# In a real application, this would interact with a database using SQLAlchemy or another ORM.