from fastapi.testclient import TestClient

from app.core.config import Settings, get_settings
from app.main import create_app


def test_agent_generate_requires_internal_service_token_when_configured() -> None:
    app = create_app()
    app.dependency_overrides[get_settings] = lambda: Settings(
        AI_INTERNAL_SERVICE_TOKEN="expected-token"
    )
    client = TestClient(app)

    response = client.post(
        "/agent/generate",
        json={
            "actorId": "member-1",
            "context": {"surface": "dashboard"},
            "input": "summarize",
        },
    )

    assert response.status_code == 401


def test_agent_generate_accepts_internal_service_token_when_configured() -> None:
    app = create_app()
    app.dependency_overrides[get_settings] = lambda: Settings(
        AI_INTERNAL_SERVICE_TOKEN="expected-token"
    )
    client = TestClient(app)

    response = client.post(
        "/agent/generate",
        headers={"X-Internal-Service-Token": "expected-token"},
        json={
            "actorId": "member-1",
            "context": {"surface": "dashboard"},
            "input": "summarize",
        },
    )

    assert response.status_code == 200


def test_health_does_not_require_internal_service_token_when_configured() -> None:
    app = create_app()
    app.dependency_overrides[get_settings] = lambda: Settings(
        AI_INTERNAL_SERVICE_TOKEN="expected-token"
    )
    client = TestClient(app)

    response = client.get("/health")

    assert response.status_code == 200
