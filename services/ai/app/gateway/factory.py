from app.core.config import Settings
from app.gateway.contracts import ModelGateway
from app.gateway.stub import StubModelGateway


def build_gateway(settings: Settings) -> ModelGateway:
    if settings.provider == "stub":
        return StubModelGateway()

    raise ValueError(f"Unsupported AI provider: {settings.provider}")
