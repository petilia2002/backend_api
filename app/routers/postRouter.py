from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.db.database import get_async_db
from app.schemas.post import PostResponse
from app.controllers.postController import PostController
from app.utils.request_parser import parse_request, PostInput

router = APIRouter(
    prefix="/posts",
    tags=["posts"],
    responses={404: {"description": "Not found"}},
)


@router.get("", response_model=List[PostResponse])
async def get_posts(db: AsyncSession = Depends(get_async_db)):
    return await PostController.get_all_posts(db)


@router.get("/{post_id}", response_model=PostResponse)
async def get_post_by_id(post_id: int, db: AsyncSession = Depends(get_async_db)):
    return await PostController.get_post_by_id(db, post_id=post_id)


@router.post("", response_model=PostResponse)
async def create_post(
    post: PostInput = Depends(parse_request),
    db: AsyncSession = Depends(get_async_db),
):
    return await PostController.create_post(db=db, post=post)


@router.delete("/{post_id}", response_model=PostResponse)
async def delete_post(post_id: int, db: AsyncSession = Depends(get_async_db)):
    return await PostController.delete_post(db, post_id)


@router.put("", response_model=PostResponse)
async def update_post(
    post: PostInput = Depends(parse_request), db: AsyncSession = Depends(get_async_db)
):
    return await PostController.update_post(db, post)
