from pydantic import BaseModel
from typing import Optional


class PostBase(BaseModel):
    author: str
    title: str
    content: str
    picture: Optional[str] = None


class PostResponse(PostBase):
    id: int

    class Config:
        from_attributes = True


class PostData(BaseModel):
    id: Optional[int] = None
    author: str
    title: str
    content: str
