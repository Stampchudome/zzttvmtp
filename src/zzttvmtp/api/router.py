from fastapi import APIRouter

from zzttvmtp.api.v1.health import health_router

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(health_router)
