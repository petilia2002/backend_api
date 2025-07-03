from sqlalchemy.orm import Session
from app.models.post import Post
from app.schemas.post import PostCreate


def get_post(db: Session, post_id: int):
    return db.query(Post).filter(Post.id == post_id).first()


def get_posts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Post).offset(skip).limit(limit).all()


def create_post(db: Session, post: PostCreate):
    db_post = Post(
        author=post.author, title=post.title, content=post.content, picture=post.picture
    )
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post
