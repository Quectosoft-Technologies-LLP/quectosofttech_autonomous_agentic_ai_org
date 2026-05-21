"""Unit tests — BaseAgent policy enforcement"""
import pytest
from src.agents.base_agent import AgentConfig
from src.core.policy_enforcer import PolicyEnforcer, PolicyViolation


@pytest.fixture
def tier4_config():
    return AgentConfig(
        agent_id="test_dev_agent",
        name="Test Developer",
        tier=4,
        department="sdlc_dev",
        role="Developer",
    )


@pytest.fixture
def tier2_config():
    return AgentConfig(
        agent_id="test_cto_agent",
        name="Test CTO",
        tier=2,
        department="executive",
        role="CTO",
    )


def test_tier4_spend_within_limit(tier4_config):
    enforcer = PolicyEnforcer(tier4_config)
    enforcer.check({"spend_usd": 500})   # should not raise


def test_tier4_spend_exceeds_limit(tier4_config):
    enforcer = PolicyEnforcer(tier4_config)
    with pytest.raises(PolicyViolation):
        enforcer.check({"spend_usd": 5000})


def test_tier2_spend_within_limit(tier2_config):
    enforcer = PolicyEnforcer(tier2_config)
    enforcer.check({"spend_usd": 40000})  # under 50000


def test_tier2_spend_exceeds_limit(tier2_config):
    enforcer = PolicyEnforcer(tier2_config)
    with pytest.raises(PolicyViolation):
        enforcer.check({"spend_usd": 60000})


def test_no_spend_key_passes(tier4_config):
    enforcer = PolicyEnforcer(tier4_config)
    enforcer.check({})   # no spend key — should pass
