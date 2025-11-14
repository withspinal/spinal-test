from urllib.parse import quote_plus

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    ENVIRONMENT: str = "local"

    # Database Settings
    DB_USER: str = Field(default="postgres")
    DB_PASSWORD: str = Field(default="password")
    DB_HOST: str = Field(default="localhost")
    DB_PORT: int = Field(default=5434)
    DB_NAME: str = Field(default="spinal")

    @property
    def database_url(self) -> str:
        encoded_password = quote_plus(self.DB_PASSWORD)
        return f"postgresql+psycopg://{self.DB_USER}:{encoded_password}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


def get_settings() -> Settings:
    """
    Get settings instance with environment-specific configuration.
    """
    return Settings()
