# src/users/repository.py
from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.users.models import User
from src.users.schemas import UserCreate, UserUpdate


class UserRepository:
    """Репозиторій для роботи з таблицею users."""

    async def get_all(
        self,
        db: AsyncSession,
        skip: int = 0,
        limit: int = 100,
    ) -> Sequence[User]:
        stmt = select(User).offset(skip).limit(limit)
        result = await db.execute(stmt)
        return result.scalars().all()

    async def get_by_id(
        self,
        db: AsyncSession,
        user_id: int,
    ) -> User | None:
        stmt = select(User).where(User.id == user_id)
        result = await db.execute(stmt)
        return result.scalars().first()

    async def get_by_email(
        self,
        db: AsyncSession,
        email: str,
    ) -> User | None:
        stmt = select(User).where(User.email == email)
        result = await db.execute(stmt)
        return result.scalars().first()

    async def create(
        self,
        db: AsyncSession,
        user_in: UserCreate,
    ) -> User:
        user = User(
            name=user_in.name,
            email=user_in.email,
        )
        db.add(user)
        await db.commit()
        await db.refresh(user)
        return user

    async def update(
        self,
        db: AsyncSession,
        user: User,
        user_in: UserUpdate,
    ) -> User:
        if user_in.name is not None:
            user.name = user_in.name
        if user_in.email is not None:
            user.email = user_in.email

        await db.commit()
        await db.refresh(user)
        return user

    async def delete(
        self,
        db: AsyncSession,
        user: User,
    ) -> None:
        await db.delete(user)
        await db.commit()
