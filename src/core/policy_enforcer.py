from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Optional
from .agent_loader import AgentLoader, AgentCard

@dataclass
class PolicyDecision:
    allowed: bool
    reason: str
    agent_id: str
    action_type: str
    resource: str
    requires_human: bool = False
    confidence_threshold: Optional[float] = None

class PolicyEnforcer:
    def __init__(self, cards: Dict[str, AgentCard]):
        self.cards = cards
    @classmethod
    def from_catalog(cls, schema_path: str | Path, catalog_root: str | Path):
        return cls(AgentLoader(schema_path, catalog_root).load_all(strict=True))
    def get_card(self, agent_id: str) -> AgentCard:
        return self.cards[agent_id]
    def can_access(self, agent_id: str, action_type: str, resource: str) -> PolicyDecision:
        card = self.get_card(agent_id)
        access = card.data.get('access', {})
        if resource in access.get('blocked', []):
            return PolicyDecision(False, f'resource explicitly blocked: {resource}', agent_id, action_type, resource)
        allowed = set(access.get(action_type, []))
        return PolicyDecision(resource in allowed, 'resource allowed by access policy' if resource in allowed else f'resource not present in access.{action_type}', agent_id, action_type, resource)
    def can_use_memory_layer(self, agent_id: str, layer: str, mode: str) -> PolicyDecision:
        granted = self.get_card(agent_id).data.get('access', {}).get('memory_layers', {}).get(layer)
        ok = (mode == 'read' and granted in {'read','write'}) or (mode == 'write' and granted == 'write')
        return PolicyDecision(ok, 'memory access allowed' if ok else f'memory {mode} denied for {layer}', agent_id, mode, layer)
    def requires_human_approval(self, agent_id: str, operation: str) -> PolicyDecision:
        approval = self.get_card(agent_id).data.get('approvalcontrol', {})
        human_required = set(approval.get('human_required_for', []))
        auto_allowed = set(approval.get('agent_auto_for', []))
        threshold = approval.get('confidence_threshold')
        if operation in human_required:
            return PolicyDecision(False, 'operation requires human approval', agent_id, 'approval', operation, True, threshold)
        if operation in auto_allowed:
            return PolicyDecision(True, 'operation allowed for agent autonomy', agent_id, 'approval', operation, False, threshold)
        return PolicyDecision(False, 'operation not explicitly approved for autonomous execution', agent_id, 'approval', operation, True, threshold)
