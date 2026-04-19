from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from zzttvmtp.api.router import api_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="zzttvmtp",
        description="AI coding agent over HTTP",
        version="0.1.0",
    )

    @app.get("/", include_in_schema=False)
    async def root() -> RedirectResponse:
        return RedirectResponse(url="/docs")

    app.include_router(api_router)

    return app


app = create_app()
