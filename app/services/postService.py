from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.post import Post
from app.schemas.post import PostCreate
from app.exceptions import ItemNotFound
from app.utils.request_parser import PostInput
from app.services.fileService import FileService


class PostService:
    @staticmethod
    async def get_all_posts(db: AsyncSession):
        result = await db.execute(select(Post).order_by(Post.id.desc()))
        return result.scalars().all()

    @staticmethod
    async def get_post_by_id(db: AsyncSession, post_id: int):
        result = await db.execute(select(Post).where(Post.id == post_id))
        post = result.scalars().first()
        if not post:
            raise ItemNotFound(post_id, "Post")
        return post

    @staticmethod
    async def create_post(db: AsyncSession, post: PostInput):
        filename = await FileService.save_upload_file(post.picture)

        db_post = Post(**{**post.data.model_dump(), "picture": filename})
        try:
            db.add(db_post)
            await db.commit()
            await db.refresh(db_post)
        except Exception:
            await db.rollback()
            raise
        return db_post
