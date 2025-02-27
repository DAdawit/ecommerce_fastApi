from fastapi_pagination import Page, Params
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from models.Products import ProductModel
from src.products.schema import ProductsOut


class ProductService:
    def __init__(self, db: Session):
        self.db = db

    async def get_all_products(
        self, page: int = 1, size: int = 10
    ) -> Page[ProductsOut]:
        params = Params(page=page, size=size)
        return paginate(self.db.query(ProductModel), params=params)

    async def create_product(self, data):
        new_product = ProductModel(
            name=data.name,
            description=data.description,
            price=data.price,
            quantity=data.quantity,
        )

        self.db.add(new_product)
        self.db.commit()
        self.db.refresh(new_product)
        return new_product
