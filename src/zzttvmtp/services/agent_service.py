from __future__ import annotations

from zzttvmtp.models.agent import CodingAgentConfig


class AgentService:
    def __init__(self) -> None:
        self._agents: dict[str, CodingAgentConfig] = {}

    def register_agent(self, config: CodingAgentConfig) -> str:
        agent_id = config.model
        self._agents[agent_id] = config
        return agent_id

    def get_agent(self, agent_id: str) -> CodingAgentConfig | None:
        return self._agents.get(agent_id)

    def list_agents(self) -> list[tuple[str, CodingAgentConfig]]:
        return list(self._agents.items())

    def plan_task(self, _agent_id: str, prompt: str) -> str:
        """Plan a coding task using the specified agent."""
        return f"Plan for: {prompt}"

    def generate_code(self, _agent_id: str, plan: str) -> str:
        """Generate code based on a plan."""
        return f"# Generated code based on: {plan}"

    def review_code(self, _agent_id: str, _code: str) -> str:
        """Review generated code."""
        return "Code looks good."
