from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from api_gestao_pessoal.database import criar_engine, criar_fabrica_sessoes
from api_gestao_pessoal.erros import registrar_tratadores_erro
from api_gestao_pessoal.rastreamento import (
    configurar_logging,
    middleware_id_requisicao,
)
from api_gestao_pessoal.routers import saude
from api_gestao_pessoal.settings import Settings, obter_settings


def criar_app(settings: Settings | None = None) -> FastAPI:
    @asynccontextmanager
    async def ciclo_de_vida(app: FastAPI) -> AsyncIterator[None]:
        s = settings or obter_settings()
        configurar_logging(s.LOG_NIVEL)
        engine = criar_engine(s)
        app.state.settings = s
        app.state.engine = engine
        app.state.fabrica_sessoes = criar_fabrica_sessoes(engine)
        try:
            yield
        finally:
            await engine.dispose()

    app = FastAPI(
        title="API MinhaVida", version="0.1.0", lifespan=ciclo_de_vida
    )
    app.middleware("http")(middleware_id_requisicao)
    registrar_tratadores_erro(app)
    app.include_router(saude.router)
    return app


app = criar_app()
