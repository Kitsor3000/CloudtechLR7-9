from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context

from src.database.base import Base
import src.users.models  # ІМПОРТУЄМО ВСІ МОДЕЛІ, щоб Alembic бачив таблиці

from src.settings import settings  # <-- ТВОЇ НАЛАШТУВАННЯ

# Конфіг Alembic (зчитує alembic.ini)
config = context.config

# Логи
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# !!! Alembic НЕ підтримує async — міняємо URL на sync
DATABASE_URL_SYNC = settings.database_url.replace("+asyncpg", "")

# Динамічно підставляємо URL у alembic.ini
config.set_main_option("sqlalchemy.url", DATABASE_URL_SYNC)

# Метадані всіх таблиць
target_metadata = Base.metadata


def run_migrations_offline():
    """Запуск міграцій у офлайн-режимі."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Запуск міграцій онлайн."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


# Запуск
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
