from fastapi import APIRouter, Depends, Query, status
from fastapi_pagination import Page
from sqlalchemy.orm import Session

from core.db import get_db
from src.users.schemas import CreateUserRequest, UserOut
from src.users.services import UserService


def get_user_service(db: Session = Depends(get_db)) -> UserService:
    return UserService(db)


router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.get("", status_code=status.HTTP_200_OK, response_model=Page[UserOut])
async def get_users(
    page: int = Query(1, ge=1, description="Page number"),
    size: int = Query(10, ge=1, le=100, description="Page size"),
    user_service: UserService = Depends(get_user_service),
) -> Page[UserOut]:
    return await user_service.get_users(page=page, size=size)


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_user(
    data: CreateUserRequest,
    user_service: UserService = Depends(get_user_service),
):
    user = await user_service.create_user_account(data)
    return user
