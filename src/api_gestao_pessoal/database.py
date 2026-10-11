from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from api_gestao_pessoal.settings import settings

if TYPE_CHECKING:
    from collections.abc import AsyncGenerator

# 1. Engine
engine = create_async_engine(settings.DATABASE_URL, hide_parameters=True)

# 2. Fábrica de Sessões (Padrão SQLAlchemy 2.0 Async)
async_session_factory = async_sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
)


# 3. Gerador de Sessão para injeção de dependência do FastAPI
async def get_session() -> AsyncGenerator[AsyncSession]:
    async with async_session_factory() as session:
        yield session
