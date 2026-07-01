from app.gateway.contracts import AgentRequest, AgentResponse, ModelGateway


class StubModelGateway(ModelGateway):
    """Deterministic gateway used until a real provider adapter is selected."""

    async def generate(self, request: AgentRequest) -> AgentResponse:
        return AgentResponse(
            provider="stub",
            output=f"Stub response for {request.context.surface}: {request.input}",
            metadata={"actorId": request.actor_id, "providerReady": False},
        )
