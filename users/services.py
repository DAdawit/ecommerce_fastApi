from fastapi.exceptions import HTTPException

from core.security import get_hasshed_password
from users.model import UserModel


async def create_user_account(data, db):
    user = db.query(UserModel).filter(UserModel.email == data.email).first()
    print(user)
    if user:
        raise HTTPException(status_code=400, detail="User already exists")
    new_user = UserModel(
        first_name=data.first_name,
        last_name=data.last_name,
        email=data.email,
        password=get_hasshed_password(data.password),
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
