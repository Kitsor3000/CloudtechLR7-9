# src/main.py
from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.database.base import Base
from src.database.session import engine
from src.users.router import router as users_router
from src.external_api.router import router as external_router  
from src.redis.router import router as redis_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    """При старті застосунку створюємо всі таблиці в БД."""
    async with engine.begin() as conn:
   
        import src.users.models  

        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(
    title="CloudTech SQL/NoSQL API",
    version="0.1.0",
    lifespan=lifespan,
)



app.include_router(users_router)  
app.include_router(external_router, prefix="/external", tags=["External"])
app.include_router(redis_router, prefix="/cache", tags=["Redis"])

@app.get("/")
async def root():
    return {
        "status": "ok",
        "message": "CloudTech API with PostgreSQL is running",
    }
