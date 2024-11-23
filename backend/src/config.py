from typing import List

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    debug: bool = Field(alias="DEBUG", default=True)
    host: str = Field(alias="API_HOST", default="localhost")
    port: int = Field(alias="API_PORT", default=8000)
    secret: SecretStr = Field(alias="SECRET_KEY")

    origins: List[str] = Field(alias="API_ORIGINS")

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


config = Settings()
