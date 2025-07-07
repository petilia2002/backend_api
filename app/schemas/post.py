from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class PostBase(BaseModel):
    author: str
    title: str
    content: str
    picture: Optional[str] = None


class PostResponse(PostBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class PostData(BaseModel):
    id: Optional[int] = None
    author: str
    title: str
    content: str
