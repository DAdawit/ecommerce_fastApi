from math import ceil

from fastapi.exceptions import HTTPException
from fastapi_pagination import Page, Params
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from core.security import get_hasshed_password
from models.Products import ProductModel
from models.User import UserModel
from src.users.schemas import UserOut


class UserService:
    def __init__(self, db: Session):
        self.db = db

    async def get_users(self, page: int = 1, size: int = 1) -> Page[UserOut]:
        params = Params(page=page, size=size)
        return paginate(self.db.query(UserModel), params=params)

    async def create_user_account(self, data):
        user = self.db.query(UserModel).filter(UserModel.email == data.email).first()
        print(user)
        if user:
            raise HTTPException(status_code=400, detail="Email already exists!")
        new_user = UserModel(
            first_name=data.first_name,
            last_name=data.last_name,
            email=data.email,
            password=get_hasshed_password(data.password),
        )

        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user
