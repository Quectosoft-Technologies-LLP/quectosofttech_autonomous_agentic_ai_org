from dataclasses import dataclass
from pathlib import Path
from src.orchestration.openclaw.approval_engine import ApprovalEngine
from .raid_entry import RAIDEntry

@dataclass
class ThresholdDecision:
    entry_id: str
    agent_id: str
    score: int
    effective_score: int
    zone: str
    action: str
    responder: str
    pause_pipeline: bool
    notify_channels: list[str]
    approval_plan: object
    threshold_source: str

class ThresholdEvaluator:
    def __init__(self, approval_engine: ApprovalEngine):
        self.approval_engine = approval_engine
    @classmethod
    def from_catalog(cls, schema_path: str | Path, catalog_root: str | Path):
        return cls(ApprovalEngine.from_catalog(schema_path, catalog_root))
    def evaluate(self, entry: RAIDEntry) -> ThresholdDecision:
        score = entry.severity_score
        if score <= 6:
            return ThresholdDecision(entry.entry_id, entry.agent_id, score, score, 'LOW', 'AUTONOMOUS', entry.agent_id, False, [], self.approval_engine.route_raid_decision(entry.agent_id, score), 'default')
        if score <= 12:
            plan = self.approval_engine.route_raid_decision(entry.agent_id, score)
            responder = plan.steps[0].agent_id if plan.steps else 'vp_review'
            return ThresholdDecision(entry.entry_id, entry.agent_id, score, score, 'MEDIUM', 'VP_REVIEW', responder, False, [], plan, 'default')
        if score <= 19:
            plan = self.approval_engine.route_raid_decision(entry.agent_id, score)
            responder = plan.steps[0].agent_id if plan.steps else 'csuite_gate'
            return ThresholdDecision(entry.entry_id, entry.agent_id, score, score, 'HIGH', 'CSUITE_GATE', responder, True, ['slack'], plan, 'default')
        return ThresholdDecision(entry.entry_id, entry.agent_id, score, score, 'CRITICAL', 'HUMAN_HITL', 'human_operator', True, ['slack','email'], self.approval_engine.route_raid_decision(entry.agent_id, score), 'default')
