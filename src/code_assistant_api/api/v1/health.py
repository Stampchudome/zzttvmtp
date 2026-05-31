from fastapi import APIRouter

health_router = APIRouter(tags=["health"])


@health_router.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "ok", "version": "0.1.0"}
