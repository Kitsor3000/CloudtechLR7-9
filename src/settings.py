from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SENTRY_DSN: str | None = None
    DATABASE_URL: str | None = None
    REDIS_URL: str | None = None

    class Config:
        env_file = ".env"


settings = Settings()
