from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete

from app.models.post import Post
from app.exceptions import ItemNotFound
from app.utils.request_parser import PostInput
from app.services.fileService import FileService
from app.db.transaction import transactional


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
        async with transactional(db):
            filename = await FileService.save_uploaded_file(post.picture)
            new_post = Post(**{**post.data.model_dump(), "picture": filename})
            db.add(new_post)
            return new_post

    @staticmethod
    async def delete_post(db: AsyncSession, post_id: int):
        result = await db.execute(select(Post).where(Post.id == post_id))
        post = result.scalar_one_or_none()
        if not post:
            raise ItemNotFound(post_id, "Post")
        if post.picture:
            await FileService.delete_file(post.picture)
        async with transactional(db):
            await db.execute(delete(Post).where(Post.id == post_id))
        return post

    @staticmethod
    async def update_post(db: AsyncSession, post: PostInput):
        id = post.data.model_dump().get("id")
        if not id:
            raise KeyError("Missing required id parameter")

        result = await db.execute(select(Post).where(Post.id == id))
        update_post = result.scalars().first()
        if not update_post:
            raise ItemNotFound(id, "Post")

        if update_post.picture:
            await FileService.delete_file(update_post.picture)
        update_post.picture = await FileService.save_uploaded_file(post.picture)

        async with transactional(db):
            update_data = post.data.model_dump(exclude_unset=True, exclude={"id"})
            for key, value in update_data.items():
                if hasattr(update_post, key):
                    setattr(update_post, key, value)
        return update_post
