import pytest

from app.gateway.contracts import AgentContext, AgentRequest
from app.gateway.stub import StubModelGateway


@pytest.mark.asyncio
async def test_stub_gateway_returns_stable_response() -> None:
    gateway = StubModelGateway()
    request = AgentRequest(
        actorId="member-1",
        context=AgentContext(surface="dashboard"),
        input="resumir próximas acciones",
    )

    response = await gateway.generate(request)

    assert response.provider == "stub"
    assert "dashboard" in response.output
    assert response.metadata["providerReady"] is False
