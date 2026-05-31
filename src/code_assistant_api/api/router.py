from fastapi import APIRouter

from code_assistant_api.api.v1.agents import agents_router
from code_assistant_api.api.v1.health import health_router
from code_assistant_api.api.v1.tasks import tasks_router

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(health_router)
api_router.include_router(tasks_router)
api_router.include_router(agents_router)
