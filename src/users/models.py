# src/users/models.py
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from src.database.base import Base, TimestampMixin


class User(Base, TimestampMixin):
    """ORM модель користувача."""

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )
    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )
    email: Mapped[str] = mapped_column(
        String(120),
        unique=True,
        index=True,
        nullable=False,
    )
