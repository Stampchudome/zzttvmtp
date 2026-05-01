from __future__ import annotations

from fastapi import APIRouter, Query

from zzttvmtp.api.v1.schemas import TaskCreateRequest, TaskResponse
from zzttvmtp.models.coding_task import TaskStatus
from zzttvmtp.services.task_service import TaskService

tasks_router = APIRouter(prefix="/tasks", tags=["tasks"])

task_service = TaskService()


@tasks_router.post("", response_model=TaskResponse, status_code=201)
async def create_task(body: TaskCreateRequest) -> TaskResponse:
    task = task_service.create_task(
        prompt=body.prompt,
        context_files=body.context_files,
        language=body.language,
    )
    return TaskResponse(id=task.id, status=task.status)


@tasks_router.get("", response_model=list[TaskResponse])
async def list_tasks(
    status: TaskStatus | None = Query(None),
    offset: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
) -> list[TaskResponse]:
    tasks = task_service.list_tasks(status=status, offset=offset, limit=limit)
    return [TaskResponse(id=t.id, status=t.status) for t in tasks]
