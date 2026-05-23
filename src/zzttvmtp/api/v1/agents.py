from __future__ import annotations

from fastapi import APIRouter

from zzttvmtp.api.errors import NotFoundError
from zzttvmtp.api.v1.schemas import (
    AgentConfigRequest,
    AgentDetailResponse,
    AgentListResponse,
)
from zzttvmtp.models.agent import CodingAgentConfig
from zzttvmtp.services.agent_service import AgentService

agents_router = APIRouter(prefix="/agents", tags=["agents"])

agent_service = AgentService()


@agents_router.get("", response_model=list[AgentListResponse])
async def list_agents() -> list[AgentListResponse]:
    agents = agent_service.list_agents()
    return [
        AgentListResponse(id=agent_id, model=config.model)
        for agent_id, config in agents
    ]


@agents_router.get("/{agent_id}", response_model=AgentDetailResponse)
async def get_agent(agent_id: str) -> AgentDetailResponse:
    config = agent_service.get_agent(agent_id)
    if config is None:
        raise NotFoundError("Agent", agent_id)
    return AgentDetailResponse(
        id=agent_id,
        model=config.model,
        temperature=config.temperature,
        max_tokens=config.max_tokens,
        system_prompt=config.system_prompt,
    )


@agents_router.post("", response_model=AgentDetailResponse, status_code=201)
async def register_agent(body: AgentConfigRequest) -> AgentDetailResponse:
    config = CodingAgentConfig(
        model=body.model,
        temperature=body.temperature,
        max_tokens=body.max_tokens,
        system_prompt=body.system_prompt,
    )
    agent_id = agent_service.register_agent(config)
    return AgentDetailResponse(
        id=agent_id,
        model=config.model,
        temperature=config.temperature,
        max_tokens=config.max_tokens,
        system_prompt=config.system_prompt,
    )
