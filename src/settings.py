from pydantic_settings import BaseSettings
from pydantic import Field



class Settings(BaseSettings):
    """Глобальні налаштування проєкту, зчитуються з .env."""

    database_url: str = Field(..., env="DATABASE_URL")  
    redis_url: str | None = Field(default=None, env="REDIS_URL")  

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
