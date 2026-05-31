from __future__ import annotations

from fastapi import Request
from fastapi.responses import JSONResponse


class AppError(Exception):
    def __init__(self, message: str, status_code: int = 500) -> None:
        self.message = message
        self.status_code = status_code


class NotFoundError(AppError):
    def __init__(self, resource: str, identifier: str) -> None:
        super().__init__(f"{resource} '{identifier}' not found", status_code=404)


class ValidationError(AppError):
    def __init__(self, message: str) -> None:
        super().__init__(message, status_code=422)


async def app_error_handler(_request: Request, exc: Exception) -> JSONResponse:
    if isinstance(exc, AppError):
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": exc.message},
        )
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"},
    )
