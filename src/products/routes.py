from typing import List

from fastapi import APIRouter, Depends, Query, status
from fastapi_pagination import Page, Params
from sqlalchemy.orm import Session

from core.db import get_db
from src.products.schema import CreateProductRequest, ProductsOut
from src.products.services import ProductService


def get_products_service(db: Session = Depends(get_db)) -> ProductService:
    return ProductService(db)


router = APIRouter(
    prefix="/products",
    tags=["products"],
    responses={404: {"description": "Not found"}},
)


@router.get("", status_code=status.HTTP_200_OK, response_model=Page[ProductsOut])
async def get_products(
    page: int = Query(1, ge=1, description="Page number"),
    size: int = Query(10, ge=1, le=100, description="Page size"),
    products_service: ProductService = Depends(get_products_service),
) -> Page[ProductsOut]:
    return await products_service.get_all_products(page=page, size=size)


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_product(
    data: CreateProductRequest,
    products_service: ProductService = Depends(get_products_service),
):
    product = await products_service.create_product(data)
    return product
