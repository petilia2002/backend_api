from sqlalchemy.orm import Session
from app.models.post import Post
from app.schemas.post import PostCreate
from sqlalchemy import desc
from app.exceptions import ItemNotFound


class PostService:
    @staticmethod
    def get_all_posts(db: Session):
        return db.query(Post).order_by(desc(Post.id)).all()

    @staticmethod
    def get_post_by_id(db: Session, post_id: int):
        post = db.query(Post).filter(Post.id == post_id).first()
        if not post:
            raise ItemNotFound(post_id, "Post")
        return post

    @staticmethod
    def create_post(db: Session, post: PostCreate):
        db_post = Post(
            author=post.author,
            title=post.title,
            content=post.content,
            picture=post.picture,
        )
        try:
            db.add(db_post)
            db.commit()
            db.refresh(db_post)
        except Exception:
            db.rollback()
            raise
        return db_post
