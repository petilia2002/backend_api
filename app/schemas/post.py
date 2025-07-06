from fastapi import UploadFile
from pydantic import BaseModel, EmailStr
from typing import List, Optional


# Для парсинга данных из json:
class PostData(BaseModel):
    author: str
    title: str
    content: str


class PostBase(BaseModel):
    author: str
    title: str
    content: str
    picture: Optional[str] = None


class PostCreate(PostBase):
    pass


class PostUpdate(BaseModel):
    author: Optional[str] = None
    title: Optional[str] = None
    content: Optional[str] = None
    picture: Optional[str] = None


class Post(PostBase):
    id: int

    class Config:
        from_attributes = True  # Ранее называлось orm_mode=True в Pydantic v1


# post = PostCreate(
#     author="petilia2002", title="defw", content="wef32f", picture="fefewf"
# )
# print(post.model_dump())

# postData = PostData(author="petnat2008", title="22323", content="228", param="222")
# print(postData)
