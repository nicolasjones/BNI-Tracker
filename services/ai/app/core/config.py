from functools import lru_cache
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Runtime configuration for the AI service."""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    service_env: str = Field(default="local", alias="AI_SERVICE_ENV")
    log_level: str = Field(default="info", alias="AI_SERVICE_LOG_LEVEL")
    provider: Literal["stub"] = Field(default="stub", alias="AI_PROVIDER")
    provider_api_key: str | None = Field(default=None, alias="AI_PROVIDER_API_KEY")
    internal_service_token: str | None = Field(
        default=None, alias="AI_INTERNAL_SERVICE_TOKEN"
    )
    supabase_url: str | None = Field(default=None, alias="SUPABASE_URL")
    supabase_service_role_key: str | None = Field(default=None, alias="SUPABASE_SERVICE_ROLE_KEY")


@lru_cache
def get_settings() -> Settings:
    return Settings()
