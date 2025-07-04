from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.schemas.post import Post, PostCreate
from app.controllers.postController import PostController

router = APIRouter(
    prefix="/posts",
    tags=["posts"],
    responses={404: {"description": "Not found"}},
)


@router.get("", response_model=List[Post])
def get_posts(db: Session = Depends(get_db)):
    return PostController.get_all_posts(db)


@router.get("/{post_id}", response_model=Post)
def get_post_by_id(post_id: int, db: Session = Depends(get_db)):
    return PostController.get_post_by_id(db, post_id=post_id)


@router.post("", response_model=Post)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    return PostController.create_post(db=db, post=post)
