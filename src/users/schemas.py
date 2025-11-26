# src/users/schemas.py
from datetime import datetime

from pydantic import BaseModel, EmailStr, ConfigDict


class UserBase(BaseModel):
    name: str
    email: EmailStr


class UserCreate(UserBase):
    """DTO для створення користувача."""
    pass


class UserUpdate(BaseModel):
    """DTO для оновлення (усі поля опційні)."""
    name: str | None = None
    email: EmailStr | None = None


class UserRead(UserBase):
    """DTO для відповіді API."""
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
