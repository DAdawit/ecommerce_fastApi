from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from core.db import get_db
from users.schemas import CreateUserRequest
from users.services import create_user_account

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_user(data: CreateUserRequest, db: Session = Depends(get_db)):
    user = await create_user_account(data, db)
    return user
