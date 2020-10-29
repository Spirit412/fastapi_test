from datetime import datetime

from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from core.db import Base


class Post(Base):
    __tablename__ = "microblog_posts"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String)
    text = Column(Text)
    date = Column(DateTime, default=datetime.now())

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="microblog_posts")