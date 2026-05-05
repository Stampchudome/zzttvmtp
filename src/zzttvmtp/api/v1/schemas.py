from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel

from zzttvmtp.models.coding_task import TaskResult, TaskStatus


class TaskCreateRequest(BaseModel):
    prompt: str
    context_files: list[str] = []
    language: str = "python"


class TaskResponse(BaseModel):
    id: str
    status: TaskStatus


class TaskDetailResponse(BaseModel):
    id: str
    prompt: str
    context_files: list[str]
    language: str
    status: TaskStatus
    created_at: datetime
    result: TaskResult | None = None
