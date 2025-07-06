from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.postService import PostService
from app.exceptions import ItemNotFound
from app.utils.request_parser import PostInput


class PostController:
    @staticmethod
    async def get_all_posts(db: AsyncSession):
        try:
            return await PostService.get_all_posts(db)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    async def get_post_by_id(db: AsyncSession, post_id: int):
        try:
            return await PostService.get_post_by_id(db, post_id)
        except ItemNotFound as e:
            raise HTTPException(status_code=404, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    async def create_post(db: AsyncSession, post: PostInput):
        try:
            return await PostService.create_post(db, post)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    async def delete_post(db: AsyncSession, post_id: int):
        try:
            return await PostService.delete_post(db, post_id)
        except ItemNotFound as e:
            raise HTTPException(status_code=404, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    async def update_post(db: AsyncSession, post: PostInput):
        try:
            return await PostService.update_post(db, post)
        except ItemNotFound as e:
            raise HTTPException(status_code=404, detail=str(e))
        except KeyError as e:
            raise HTTPException(status_code=400, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
