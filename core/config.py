import os
from pathlib import Path
from urllib.parse import quote_plus

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

env_path = Path(".") / ".env"

load_dotenv(dotenv_path=env_path)


class Settings(BaseSettings):
    # Database
    DB_USER: str = str(os.getenv("DB_USER"))
    DB_PASSWORD: str = str(os.getenv("DB_PASSWORD"))
    DB_HOST: str = str(os.getenv("DB_HOST"))
    DB_PORT: str = str(os.getenv("DB_PORT"))
    DB_NAME: str = str(os.getenv("DB_NAME"))
    DB_URL: str = (
        f"mysql+pymysql://{DB_USER}:{quote_plus(DB_PASSWORD)}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )


def get_settings() -> Settings:
    return Settings()

    # # Redis
    # REDIS_HOST: str
    # REDIS_PORT: str
    # REDIS_DB: int

    # # JWT
    # JWT_SECRET_KEY: str
    # JWT_ALGORITHM: str
    # JWT_EXPIRE_MINUTES: int

    # # Email
    # EMAIL_USER: str
    # EMAIL_PASSWORD: str
    # EMAIL_PORT: str
    # EMAIL_SMTP: str

    # # App
    # APP_HOST: str
    # APP_PORT: str
    # APP_NAME: str
    # APP_ENV: str

    # # Debug
    # DEBUG: bool

    # class Config:
    #     env_file = env_path
