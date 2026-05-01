from __future__ import annotations

from pydantic import BaseModel

from zzttvmtp.models.coding_task import TaskStatus


class TaskCreateRequest(BaseModel):
    prompt: str
    context_files: list[str] = []
    language: str = "python"


class TaskResponse(BaseModel):
    id: str
    status: TaskStatus
