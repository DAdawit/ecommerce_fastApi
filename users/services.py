from math import ceil

from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from core.security import get_hasshed_password
from models.User import UserModel
from utils.paginate import paginate


class UserService:
    def __init__(self, db: Session):
        self.db = db

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

    async def get_users(self, page: int = 1, per_page: int = 20):
        try:
            query = self.db.query(UserModel)
            return paginate(query, self.db, page=page, per_page=per_page)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
