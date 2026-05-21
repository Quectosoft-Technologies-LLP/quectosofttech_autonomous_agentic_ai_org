"""Unit tests — RAIDScorer and ThresholdEvaluator"""
import pytest
from src.raid.raid_entry import RAIDEntry, RAIDType, RAIDArea
from src.raid.raid_scorer import RAIDScorer
from src.raid.threshold_evaluator import ThresholdEvaluator, ThresholdConfig


@pytest.fixture
def scorer():
    return RAIDScorer()


@pytest.fixture
def evaluator():
    return ThresholdEvaluator(ThresholdConfig(
        auto_mitigate_below=7,
        vp_review_from=7,
        csuite_gate_from=13,
        human_hitl_from=20,
    ))


def make_entry(likelihood: int, impact: int) -> RAIDEntry:
    return RAIDEntry(
        agent_id="test_agent",
        raid_type=RAIDType.RISK,
        area=RAIDArea.TECHNICAL,
        description="Test risk",
        likelihood=likelihood,
        impact=impact,
    )


def test_score_low(scorer):
    assert scorer.score(make_entry(1, 2)) == 2


def test_score_max(scorer):
    assert scorer.score(make_entry(5, 5)) == 25


def test_zone_low(scorer):
    assert scorer.zone(4) == "LOW"


def test_zone_medium(scorer):
    assert scorer.zone(9) == "MEDIUM"


def test_zone_high(scorer):
    assert scorer.zone(15) == "HIGH"


def test_zone_critical(scorer):
    assert scorer.zone(21) == "CRITICAL"


def test_threshold_auto(evaluator):
    assert evaluator.evaluate(make_entry(1, 1)) == "AUTO_MITIGATE"


def test_threshold_vp(evaluator):
    assert evaluator.evaluate(make_entry(2, 4)) == "VP_REVIEW"   # score=8


def test_threshold_csuite(evaluator):
    assert evaluator.evaluate(make_entry(3, 5)) == "CSUITE_GATE"  # score=15


def test_threshold_hitl(evaluator):
    assert evaluator.evaluate(make_entry(5, 4)) == "HUMAN_HITL"   # score=20


def test_severity_auto_calculated():
    entry = make_entry(3, 4)
    assert entry.severity == 12
