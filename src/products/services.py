from sqlalchemy.orm import Session

from models.Products import ProductModel


class ProductService:
    def __init__(self, db: Session):
        self.db = db

    async def get_all_products(self):
        return self.db.query(ProductModel).all()

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
