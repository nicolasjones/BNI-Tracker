import pytest
from pydantic import ValidationError

from app.gateway.contracts import AgentContext, AgentRequest


def test_agent_request_requires_actor_and_input() -> None:
    with pytest.raises(ValidationError):
        AgentRequest(actorId="", context=AgentContext(surface="dashboard"), input="")


def test_agent_request_accepts_product_contract_alias() -> None:
    request = AgentRequest(
        actorId="member-1",
        context={"surface": "contact", "entity_id": "contact-1"},
        input="preparar seguimiento",
    )

    assert request.actor_id == "member-1"
    assert request.context.surface == "contact"
