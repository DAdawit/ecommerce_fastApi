from fastapi import Depends, FastAPI
from fastapi_pagination import Page, add_pagination
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from core.db import get_db
from models.Products import ProductModel
from src.products.routes import router as products_router
from src.products.schema import ProductsOut
from src.users.routes import router as users_router

app = FastAPI()

app.include_router(users_router)
app.include_router(products_router)

add_pagination(app)


@app.get("/")
def home():
    return {"message": "Hello World"}
