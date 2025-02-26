from fastapi import FastAPI

from src.products.routes import router as products_router
from src.users.routes import router as users_router

# from src.products.routes import router as products_router
# from src.users.routes import router as users_router

app = FastAPI()

app.include_router(users_router)
app.include_router(products_router)


@app.get("/")
def home():
    return {"message": "Hello World"}
