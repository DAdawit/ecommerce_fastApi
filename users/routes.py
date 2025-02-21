from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from core.db import get_db
from users.schemas import CreateUserRequest
from users.services import UserService


def get_user_service(db: Session = Depends(get_db)) -> UserService:
    return UserService(db)


router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_user(
    data: CreateUserRequest,
    user_service: UserService = Depends(get_user_service),
):
    user = await user_service.create_user_account(data)
    return user


@router.get("", status_code=status.HTTP_200_OK)
async def get_users(UserService: UserService = Depends(get_user_service)):
    users = await UserService.get_users()
    return users
