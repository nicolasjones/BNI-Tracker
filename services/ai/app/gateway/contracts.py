from typing import Protocol

from pydantic import BaseModel, Field


class AgentContext(BaseModel):
    surface: str = Field(min_length=1)
    entity_id: str | None = None


class AgentRequest(BaseModel):
    actor_id: str = Field(min_length=1, alias="actorId")
    context: AgentContext
    input: str = Field(min_length=1, max_length=12000)


class AgentResponse(BaseModel):
    provider: str
    output: str
    metadata: dict[str, str | int | float | bool] = Field(default_factory=dict)


class ModelGateway(Protocol):
    async def generate(self, request: AgentRequest) -> AgentResponse:
        """Generate an answer from a provider-specific implementation."""
