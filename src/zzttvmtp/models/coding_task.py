from __future__ import annotations

from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, Field


class TaskStatus(StrEnum):
    pending = "pending"
    planning = "planning"
    generating = "generating"
    reviewing = "reviewing"
    completed = "completed"
    failed = "failed"


class TaskResult(BaseModel):
    summary: str
    files_changed: list[str] = []
    error_message: str | None = None


class CodingTask(BaseModel):
    id: str
    prompt: str
    context_files: list[str] = []
    language: str = "python"
    status: TaskStatus = TaskStatus.pending
    created_at: datetime = Field(default_factory=datetime.now)
    result: TaskResult | None = None
