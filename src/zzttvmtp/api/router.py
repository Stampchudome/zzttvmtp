from fastapi import APIRouter

from zzttvmtp.api.v1.health import health_router
from zzttvmtp.api.v1.tasks import tasks_router

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(health_router)
api_router.include_router(tasks_router)
