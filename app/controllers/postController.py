from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.schemas.post import PostCreate
from app.services.postService import PostService
from app.exceptions import ItemNotFound


class PostController:
    @staticmethod
    def get_all_posts(db: Session):
        try:
            return PostService.get_all_posts(db)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_post_by_id(db: Session, post_id: int):
        try:
            return PostService.get_post_by_id(db, post_id)
        except ItemNotFound as e:
            raise HTTPException(status_code=404, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def create_post(db: Session, post: PostCreate):
        try:
            return PostService.create_post(db, post)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
