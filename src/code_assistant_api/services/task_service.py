from __future__ import annotations

import uuid
from datetime import datetime

from code_assistant_api.models.coding_task import CodingTask, TaskStatus


class TaskService:
    def __init__(self) -> None:
        self._tasks: dict[str, CodingTask] = {}

    def create_task(
        self,
        prompt: str,
        context_files: list[str] | None = None,
        language: str = "python",
    ) -> CodingTask:
        task = CodingTask(
            id=str(uuid.uuid4()),
            prompt=prompt,
            context_files=context_files or [],
            language=language,
            status=TaskStatus.pending,
            created_at=datetime.now(),
        )
        self._tasks[task.id] = task
        return task

    def get_task(self, task_id: str) -> CodingTask | None:
        return self._tasks.get(task_id)

    def list_tasks(
        self,
        status: TaskStatus | None = None,
        offset: int = 0,
        limit: int = 100,
    ) -> list[CodingTask]:
        tasks = list(self._tasks.values())
        if status is not None:
            tasks = [t for t in tasks if t.status == status]
        return tasks[offset : offset + limit]

    def update_task_status(self, task_id: str, status: TaskStatus) -> CodingTask | None:
        task = self._tasks.get(task_id)
        if task is None:
            return None
        task.status = status
        return task

    def delete_task(self, task_id: str) -> bool:
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False
