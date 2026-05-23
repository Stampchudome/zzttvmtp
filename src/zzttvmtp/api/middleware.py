from __future__ import annotations

import time

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response


class RequestTimingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):  # type: ignore[no-untyped-def]
        start = time.monotonic()
        response: Response = await call_next(request)
        elapsed = time.monotonic() - start
        response.headers["X-Request-Time-Ms"] = str(round(elapsed * 1000, 2))
        return response
