from __future__ import annotations

import os
from collections.abc import AsyncIterator

import pytest
from httpx import ASGITransport, AsyncClient

# Allow pydantic-ai to initialize without real credentials in tests
os.environ.setdefault("OPENAI_API_KEY", "sk-test-fake-key")

from code_assistant_api.main import app  # noqa: E402


@pytest.fixture
async def client() -> AsyncIterator[AsyncClient]:
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac


@pytest.fixture
def sample_task_payload() -> dict[str, object]:
    return {
        "prompt": "Write a function to sort a list of integers.",
        "language": "python",
    }
