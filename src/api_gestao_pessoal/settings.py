import functools
from typing import Literal

from pydantic import Field, SecretStr, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        hide_input_in_errors=True,
    )

    DATABASE_URL: SecretStr
    AMBIENTE: Literal["desenvolvimento", "teste", "producao"] = (
        "desenvolvimento"
    )
    LOG_NIVEL: Literal["DEBUG", "INFO", "WARNING", "ERROR"] = "INFO"
    DB_POOL_SIZE: int = Field(default=5, ge=1, le=50)
    DB_MAX_OVERFLOW: int = Field(default=5, ge=0, le=50)
    DB_POOL_TIMEOUT_S: float = Field(default=10, gt=0)
    DB_CONNECT_TIMEOUT_S: int = Field(default=5, ge=1, le=60)
    DB_STATEMENT_TIMEOUT_MS: int = Field(default=15000, ge=100)
    DB_LOCK_TIMEOUT_MS: int = Field(default=5000, ge=50)
    DB_IDLE_IN_TRANSACTION_TIMEOUT_MS: int = Field(default=30000, ge=1000)

    @field_validator("DATABASE_URL")
    @classmethod
    def validar_esquema_da_url(cls, valor: SecretStr) -> SecretStr:
        if not valor.get_secret_value().startswith("postgresql+psycopg://"):
            msg = "DATABASE_URL deve usar o esquema postgresql+psycopg://"
            raise ValueError(msg)
        return valor


@functools.lru_cache(maxsize=1)
def obter_settings() -> Settings:
    # DATABASE_URL é obrigatório e vem do ambiente / .env, não de argumentos;
    # o Pyright só enxerga os parâmetros do __init__ sintetizado.
    return Settings()  # pyright: ignore[reportCallIssue]
