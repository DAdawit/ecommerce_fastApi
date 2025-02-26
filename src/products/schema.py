from datetime import datetime

import sqlalchemy
from pydantic import BaseModel, Field


class CreateProductRequest(BaseModel):
    name: str = Field(..., min_length=2, max_length=50, examples=["Product Name"])
    description: str = Field(
        ..., min_length=2, max_length=100, examples=["Product Description"]
    )
    price: float = Field(..., gt=0, examples=[100.0])
    quantity: int = Field(..., gt=0, examples=[100])


class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int

    class Config:
        orm_mode = True


class ProductsOut(BaseModel):
    is_available: bool
    name: str
    description: str
    created_at: datetime
    price: float
    id: int
    quantity: int
    updated_at: datetime | None = None

    class Config:
        orm_mode = True
