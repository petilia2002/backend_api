from fastapi import FastAPI
from app.routers import posts
from app.db.database import engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(
    title="My FastAPI App",
    description="A sample FastAPI application with well-organized structure",
    version="0.1.0",
)

# Include routers
app.include_router(posts.router, prefix="/api")


@app.get("/")
async def root():
    return {"message": "Welcome to my FastAPI application!"}
