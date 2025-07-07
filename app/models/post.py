from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.db.database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    author = Column(String(50), nullable=False)
    title = Column(String(100), nullable=False)
    content = Column(String(500), nullable=False)
    picture = Column(String(100))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
