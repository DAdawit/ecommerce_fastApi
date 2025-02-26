from typing import List

from fastapi import APIRouter, Depends, Query, status
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


@router.get("", status_code=status.HTTP_200_OK, response_model=List[ProductsOut])
async def get_products(
    products_service: ProductService = Depends(get_products_service),
) -> List[ProductsOut]:
    return await products_service.get_all_products()


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_product(
    data: CreateProductRequest,
    products_service: ProductService = Depends(get_products_service),
):
    product = await products_service.create_product(data)
    return product
