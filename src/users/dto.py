from pydantic import BaseModel, EmailStr, Field


class UserCreateDTO(BaseModel):
    name: str = Field(..., min_length=2)
    email: EmailStr


class UserUpdateDTO(BaseModel):
    name: str | None = Field(None, min_length=2)
    email: EmailStr | None = None
