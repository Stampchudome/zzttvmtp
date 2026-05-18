from __future__ import annotations

from httpx import AsyncClient


async def test_create_task_returns_id(
    client: AsyncClient, sample_task_payload: dict[str, object]
) -> None:
    response = await client.post("/api/v1/tasks", json=sample_task_payload)
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["status"] == "pending"


async def test_list_tasks(
    client: AsyncClient, sample_task_payload: dict[str, object]
) -> None:
    await client.post("/api/v1/tasks", json=sample_task_payload)
    response = await client.get("/api/v1/tasks")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1


async def test_get_task_by_id(
    client: AsyncClient, sample_task_payload: dict[str, object]
) -> None:
    create_resp = await client.post("/api/v1/tasks", json=sample_task_payload)
    task_id = create_resp.json()["id"]

    response = await client.get(f"/api/v1/tasks/{task_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == task_id
    assert data["prompt"] == sample_task_payload["prompt"]
