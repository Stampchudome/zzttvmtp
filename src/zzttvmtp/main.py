from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from starlette.middleware.cors import CORSMiddleware

from zzttvmtp.api.errors import AppError, app_error_handler
from zzttvmtp.api.middleware import RequestTimingMiddleware
from zzttvmtp.api.router import api_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="zzttvmtp",
        description="AI coding agent over HTTP",
        version="0.1.0",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.add_middleware(RequestTimingMiddleware)

    app.add_exception_handler(AppError, app_error_handler)

    @app.get("/", include_in_schema=False)
    async def root() -> RedirectResponse:
        return RedirectResponse(url="/docs")

    app.include_router(api_router)

    return app


app = create_app()
