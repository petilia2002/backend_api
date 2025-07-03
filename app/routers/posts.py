from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.schemas.post import Post, PostCreate
from app.crud import post as post_crud

router = APIRouter(
    prefix="/posts",
    tags=["posts"],
    responses={404: {"description": "Not found"}},
)


@router.get("", response_model=List[Post])
def read_posts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    posts = post_crud.get_posts(db, skip=skip, limit=limit)
    return posts


@router.post("", response_model=Post)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    db_post = post_crud.create_post(db=db, post=post)
    if not db_post:
        raise HTTPException(status_code=500, detail="Couldn't create a post")
    return db_post


@router.get("/{post_id}", response_model=Post)
def read_post(post_id: int, db: Session = Depends(get_db)):
    db_post = post_crud.get_post(db, post_id=post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post
