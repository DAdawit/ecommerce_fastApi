from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from core.config import get_settings

settings = get_settings()

engin = create_engine(
    settings.DB_URL,
    pool_pre_ping=True,
    pool_size=10,
    max_overflow=0,
    pool_recycle=3600,
    echo=True,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engin)
Base = declarative_base()


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
