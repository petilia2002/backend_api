from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from contextlib import asynccontextmanager
from sqlalchemy.ext.declarative import declarative_base
from app.core.config import DATABASE_URL

# Асинхронный движок (для PostgreSQL используем asyncpg)
async_engine = create_async_engine(
    DATABASE_URL.replace("postgresql+psycopg2://", "postgresql+asyncpg://"),
    echo=True,  # Логирование запросов (можно отключить)
)

# Асинхронная сессия
AsyncSessionLocal = sessionmaker(
    bind=async_engine, class_=AsyncSession, expire_on_commit=False, autoflush=False
)

Base = declarative_base()


async def get_async_db():
    async with AsyncSessionLocal() as db:
        try:
            yield db
        finally:
            await db.close()
