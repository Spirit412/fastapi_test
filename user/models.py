from datetime import datetime

from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Text, Boolean
from sqlalchemy.orm import relationship
from core.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    date = Column(DateTime, default=datetime.now())
    is_admin = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)

    # post = relationship("Post", back_populates="user")
