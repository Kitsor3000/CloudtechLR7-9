# src/database/session.py
from collections.abc import AsyncIterator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from src.settings import settings
from src.database.base import Base

# створюємо async engine
engine = create_async_engine(
    settings.database_url,
    echo=True,          # можна вимкнути в бойовому оточенні
    future=True,
)

# фабрика сесій
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


async def get_db() -> AsyncIterator[AsyncSession]:
    """Dependency для FastAPI роутів (yield дає сесію в ендпоінт)."""
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
