from pydantic import BaseModel


class AgentCapability(BaseModel):
    type: str  # analysis | codegen | review


class CodingAgentConfig(BaseModel):
    model: str = "gpt-4o"
    temperature: float = 0.2
    max_tokens: int = 4096
    system_prompt: str = "You are a helpful coding assistant."
