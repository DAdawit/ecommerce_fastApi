from datetime import datetime

from pydantic import BaseModel, EmailStr, Field


class CreateUserRequest(BaseModel):
    first_name: str = Field(..., min_length=2, max_length=50, examples=["John"])
    last_name: str = Field(..., min_length=2, max_length=50, examples=["Doe"])
    email: EmailStr = Field(..., examples=["john.doe@example.com"])
    password: str = Field(
        ..., min_length=8, max_length=100, examples=["StrongPass123!"]
    )


class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str

    class Config:
        orm_mode = True


from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class UserOut(BaseModel):
    id: int
    email: EmailStr
    first_name: str
    last_name: str
    is_active: bool
    is_verified: bool
    created_at: datetime
    updated_at: datetime | None = None
    verified_at: datetime | None = None

    class Config:
        orm_mode = True  # Allows ORM mode for SQLAlchemy compatibility
