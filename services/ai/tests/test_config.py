import pytest
from pydantic import ValidationError

from app.core.config import Settings


def test_settings_default_to_stub_provider() -> None:
    settings = Settings()

    assert settings.provider == "stub"
    assert settings.service_env == "local"


def test_settings_reject_unknown_provider() -> None:
    with pytest.raises(ValidationError):
        Settings(AI_PROVIDER="unknown")
