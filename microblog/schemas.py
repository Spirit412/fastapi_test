from pydantic import BaseModel
from datetime import datetime


class PostBase(BaseModel):
    title: str
    text: str
    # date: datetime #убрал необходимость писать datetime. datetime генерится в модели по default=datetime.now()

    class Config:
        orm_mode = True


class PostList(PostBase):
    id: int
    date: datetime


class PostCreate(PostBase):
    pass
