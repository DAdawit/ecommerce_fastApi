from pydantic import BaseModel, EmailStr, Field


class CreateUserRequest(BaseModel):
    first_name: str = Field(..., min_length=2, max_length=50, examples=["John"])
    last_name: str = Field(..., min_length=2, max_length=50, examples=["Doe"])
    email: EmailStr = Field(..., examples=["john.doe@example.com"])
    password: str = Field(
        ..., min_length=8, max_length=100, examples=["StrongPass123!"]
    )
