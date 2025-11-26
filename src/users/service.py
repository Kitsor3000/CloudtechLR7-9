# src/users/service.py
from sqlalchemy.ext.asyncio import AsyncSession

from src.users.repository import UserRepository
from src.users.schemas import UserCreate, UserUpdate
from src.users.models import User


class UserService:
    def __init__(self, repo: UserRepository | None = None):
        self.repo = repo or UserRepository()

    async def list_users(
        self,
        db: AsyncSession,
        skip: int = 0,
        limit: int = 100,
    ) -> list[User]:
        return list(await self.repo.get_all(db, skip=skip, limit=limit))

    async def get_user(
        self,
        db: AsyncSession,
        user_id: int,
    ) -> User | None:
        return await self.repo.get_by_id(db, user_id)

    async def create_user(
        self,
        db: AsyncSession,
        user_in: UserCreate,
    ) -> User:
        # Перевірка унікальності email
        existing = await self.repo.get_by_email(db, user_in.email)
        if existing:
            raise ValueError("User with this email already exists")
        return await self.repo.create(db, user_in)

    async def update_user(
        self,
        db: AsyncSession,
        user_id: int,
        user_in: UserUpdate,
    ) -> User | None:
        user = await self.repo.get_by_id(db, user_id)
        if not user:
            return None
        return await self.repo.update(db, user, user_in)

    async def delete_user(
        self,
        db: AsyncSession,
        user_id: int,
    ) -> bool:
        user = await self.repo.get_by_id(db, user_id)
        if not user:
            return False
        await self.repo.delete(db, user)
        return True
