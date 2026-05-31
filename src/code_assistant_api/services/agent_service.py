from __future__ import annotations

from code_assistant_api.models.agent import CodingAgentConfig
from code_assistant_api.services.coding_agent import CodingAgent


class AgentService:
    def __init__(self) -> None:
        self._agents: dict[str, CodingAgentConfig] = {}
        self._instances: dict[str, CodingAgent] = {}

    def register_agent(self, config: CodingAgentConfig) -> str:
        agent_id = config.model
        self._agents[agent_id] = config
        self._instances[agent_id] = CodingAgent(config)
        return agent_id

    def get_agent(self, agent_id: str) -> CodingAgentConfig | None:
        return self._agents.get(agent_id)

    def list_agents(self) -> list[tuple[str, CodingAgentConfig]]:
        return list(self._agents.items())

    def get_coding_agent(self, agent_id: str) -> CodingAgent | None:
        return self._instances.get(agent_id)

    async def plan_task(self, agent_id: str, prompt: str) -> str:
        agent = self._instances.get(agent_id)
        if agent is None:
            return "No agent configured."
        return await agent.plan(prompt)

    async def generate_code(self, agent_id: str, prompt: str, plan: str) -> str:
        agent = self._instances.get(agent_id)
        if agent is None:
            return "# No agent configured."
        result = await agent.execute(prompt, plan)
        return result.code

    async def review_code(self, _agent_id: str, _code: str) -> str:
        return "Review not yet implemented."
