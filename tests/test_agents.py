from __future__ import annotations

from httpx import AsyncClient


async def test_list_agents_empty(client: AsyncClient) -> None:
    response = await client.get("/api/v1/agents")
    assert response.status_code == 200
    assert response.json() == []


async def test_register_and_get_agent(client: AsyncClient) -> None:
    payload = {
        "model": "gpt-4o",
        "temperature": 0.3,
        "max_tokens": 2048,
        "system_prompt": "You are a code reviewer.",
    }
    create_resp = await client.post("/api/v1/agents", json=payload)
    assert create_resp.status_code == 201
    agent_id = create_resp.json()["id"]

    get_resp = await client.get(f"/api/v1/agents/{agent_id}")
    assert get_resp.status_code == 200
    assert get_resp.json()["model"] == "gpt-4o"
    assert get_resp.json()["temperature"] == 0.3


async def test_get_agent_not_found(client: AsyncClient) -> None:
    response = await client.get("/api/v1/agents/nonexistent")
    assert response.status_code == 404
