from __future__ import annotations

from pydantic import BaseModel
from pydantic_ai import Agent, ModelSettings

from code_assistant_api.models.agent import CodingAgentConfig


class CodeOutput(BaseModel):
    plan: str
    code: str
    explanation: str
    files: list[str] = []


class CodingAgent:
    def __init__(self, config: CodingAgentConfig) -> None:
        self.config = config
        settings = ModelSettings(
            temperature=config.temperature,
            max_tokens=config.max_tokens,
        )
        self._agent: Agent[None, CodeOutput] = Agent(
            model=config.model,
            system_prompt=config.system_prompt,
            output_type=CodeOutput,
            model_settings=settings,
        )

    async def plan(self, prompt: str, context: str | None = None) -> str:
        full_prompt = f"Plan the implementation for: {prompt}"
        if context:
            full_prompt += f"\n\nContext:\n{context}"
        result = await self._agent.run(full_prompt)
        return result.output.plan

    async def execute(self, prompt: str, plan: str) -> CodeOutput:
        full_prompt = f"Prompt: {prompt}\n\nPlan: {plan}\n\nGenerate the implementation."
        result = await self._agent.run(full_prompt)
        return result.output
