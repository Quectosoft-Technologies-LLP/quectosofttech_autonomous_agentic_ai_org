"""Unit tests — ModelRouter"""
import pytest
from src.agents.base_agent import AgentConfig
from src.core.model_router import ModelRouter


@pytest.fixture
def config():
    return AgentConfig(
        agent_id="test_agent",
        name="Test Agent",
        tier=4,
        department="sdlc",
        role="Developer",
        model_default="hermes3:8b",
        model_critical="claude-opus-4",
    )


def test_default_model(config):
    router = ModelRouter(config)
    assert router.select({}) == "hermes3:8b"


def test_critical_task(config):
    router = ModelRouter(config)
    assert router.select({"complexity": "critical"}) == "claude-opus-4"


def test_high_complexity(config):
    router = ModelRouter(config)
    result = router.select({"complexity": "high"})
    assert "70b" in result or "claude" in result


def test_low_complexity(config):
    router = ModelRouter(config)
    result = router.select({"complexity": "low"})
    assert "1b" in result


def test_offline_only_uses_advanced(config):
    router = ModelRouter(config)
    result = router.select({"offline_only": True})
    assert "70b" in result
