from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

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


class AgentConfigRequest(BaseModel):
    model: str = "gpt-4o"
    temperature: float = Field(default=0.2, ge=0.0, le=2.0)
    max_tokens: int = Field(default=4096, ge=1, le=128_000)
    system_prompt: str = "You are a helpful coding assistant."


class AgentListResponse(BaseModel):
    id: str
    model: str


class AgentDetailResponse(BaseModel):
    id: str
    model: str
    temperature: float
    max_tokens: int
    system_prompt: str
