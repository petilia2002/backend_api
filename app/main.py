from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
from app.routers import postRouter
from app.db.database import async_engine, Base  # Импортируем async_engine вместо engine
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR.parent / "static"


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Код, выполняемый при запуске приложения
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # Код, выполняемый при остановке приложения (опционально)
    await async_engine.dispose()


app = FastAPI(
    title="My FastAPI App",
    description="A sample FastAPI application with well-organized structure",
    version="0.1.0",
    lifespan=lifespan,
)

# Включаем выдачу статичных файлов
app.mount("/static", StaticFiles(directory=STATIC_DIR), "static")

# Включаем асинхронные роутеры
app.include_router(postRouter.router, prefix="/api")


# Асинхронный корневой эндпоинт
@app.get("/")
async def root():
    return {"Message": "Welcome to my FastAPI application!"}
