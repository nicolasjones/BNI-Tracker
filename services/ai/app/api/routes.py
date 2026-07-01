from fastapi import APIRouter, Depends, Header, HTTPException, status

from app.core.config import Settings, get_settings
from app.gateway.contracts import AgentRequest, AgentResponse
from app.gateway.factory import build_gateway

router = APIRouter()


def require_internal_service_token(
    settings: Settings = Depends(get_settings),
    x_internal_service_token: str | None = Header(default=None),
) -> None:
    expected_token = settings.internal_service_token
    if not expected_token:
        return

    if x_internal_service_token != expected_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing or invalid internal service token",
        )


@router.get("/health")
def health(settings: Settings = Depends(get_settings)) -> dict[str, str]:
    return {"status": "ok", "service": "ai", "environment": settings.service_env}


@router.post(
    "/agent/generate",
    response_model=AgentResponse,
    dependencies=[Depends(require_internal_service_token)],
)
async def generate_agent_response(
    request: AgentRequest,
    settings: Settings = Depends(get_settings),
) -> AgentResponse:
    gateway = build_gateway(settings)
    return await gateway.generate(request)
