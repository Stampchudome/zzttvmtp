from __future__ import annotations

from fastapi import APIRouter, Query

from code_assistant_api.api.errors import NotFoundError
from code_assistant_api.api.v1.schemas import (
    TaskCreateRequest,
    TaskDetailResponse,
    TaskResponse,
)
from code_assistant_api.models.coding_task import TaskStatus
from code_assistant_api.services.task_service import TaskService

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


@tasks_router.get("/{task_id}", response_model=TaskDetailResponse)
async def get_task(task_id: str) -> TaskDetailResponse:
    task = task_service.get_task(task_id)
    if task is None:
        raise NotFoundError("Task", task_id)
    return TaskDetailResponse(
        id=task.id,
        prompt=task.prompt,
        context_files=task.context_files,
        language=task.language,
        status=task.status,
        created_at=task.created_at,
        result=task.result,
    )


@tasks_router.delete("/{task_id}", status_code=204)
async def delete_task(task_id: str) -> None:
    deleted = task_service.delete_task(task_id)
    if not deleted:
        raise NotFoundError("Task", task_id)
    return None
