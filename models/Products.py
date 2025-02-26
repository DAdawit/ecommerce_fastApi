from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer, String, func

from core.db import Base


class ProductModel(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    description = Column(String(500))
    price = Column(Integer)
    is_available = Column(Boolean, default=True)
    quantity = Column(Integer)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, nullable=True, default=None, onupdate=func.now())
