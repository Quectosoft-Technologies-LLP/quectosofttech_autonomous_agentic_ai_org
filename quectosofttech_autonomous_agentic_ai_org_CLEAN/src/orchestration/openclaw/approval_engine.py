from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional
from src.core.agent_loader import AgentLoader, AgentCard
from src.core.policy_enforcer import PolicyEnforcer

@dataclass
class ApprovalStep:
    agent_id: str
    reason: str
    tier: Optional[int]
    step_type: str

@dataclass
class ApprovalPlan:
    requester: str
    operation: str
    requires_human: bool
    final_decision: str
    steps: List[ApprovalStep]
    confidence_threshold: Optional[float] = None

class ApprovalEngine:
    HUMAN_SENTINELS = {'human_operator','human','board','shareholders'}
    def __init__(self, cards: Dict[str, AgentCard], policy_enforcer: PolicyEnforcer):
        self.cards = cards; self.policy_enforcer = policy_enforcer
    @classmethod
    def from_catalog(cls, schema_path: str | Path, catalog_root: str | Path):
        loader = AgentLoader(schema_path, catalog_root); cards = loader.load_all(strict=True); return cls(cards, PolicyEnforcer(cards))
    def get_card(self, agent_id: str) -> AgentCard:
        return self.cards[agent_id]
    def resolve_chain(self, start_agent_id: str, field: str='reportsto', max_depth: int=12) -> List[ApprovalStep]:
        chain=[]; visited={start_agent_id}; current=start_agent_id
        for _ in range(max_depth):
            target = self.get_card(current).data.get(field)
            if not target: break
            if target in self.HUMAN_SENTINELS: chain.append(ApprovalStep(target, f'{field} terminal human sentinel', None, 'human')); return chain
            if target in visited: chain.append(ApprovalStep(target, f'cycle detected in {field} chain', None, 'cycle')); return chain
            if target not in self.cards: chain.append(ApprovalStep(target, f'{field} unresolved target', None, 'unresolved')); return chain
            tc = self.get_card(target); chain.append(ApprovalStep(target, f'{field} hop', tc.data.get('tier'), 'agent')); visited.add(target); current=target
        return chain
    def get_operation_plan(self, requester: str, operation: str) -> ApprovalPlan:
        d = self.policy_enforcer.requires_human_approval(requester, operation); steps=[]
        if d.requires_human:
            chain=self.resolve_chain(requester,'escalationto'); steps.extend(chain); terminal = chain[-1].step_type if chain else 'human'
            final = 'HUMAN_REQUIRED' if terminal=='human' else ('ROUTING_FIX_REQUIRED' if terminal in {'cycle','unresolved','limit'} else 'ESCALATE_TO_AGENT')
        else:
            final='AUTO_APPROVED'; manager=self.get_card(requester).data.get('reportsto')
            if manager and manager in self.cards: steps.append(ApprovalStep(manager, 'manager visibility', self.get_card(manager).data.get('tier'), 'notify'))
        return ApprovalPlan(requester, operation, d.requires_human, final, steps, d.confidence_threshold)
    def route_raid_decision(self, requester: str, severity_score: int) -> ApprovalPlan:
        if severity_score <= 6: return ApprovalPlan(requester, 'raid_autonomous', False, 'AUTO_APPROVED', [], None)
        if 7 <= severity_score <= 12:
            chain=self.resolve_chain(requester,'reportsto'); step=next((s for s in chain if s.tier==3), chain[0] if chain else ApprovalStep('human_operator','fallback',None,'human'))
            return ApprovalPlan(requester, 'raid_vp_review', False, 'VP_REVIEW' if step.step_type not in {'cycle','unresolved','limit'} else 'ROUTING_FIX_REQUIRED', [step], None)
        if 13 <= severity_score <= 19:
            chain=self.resolve_chain(requester,'escalationto'); step=next((s for s in chain if s.tier==2), chain[-1] if chain else ApprovalStep('human_operator','fallback',None,'human'))
            return ApprovalPlan(requester, 'raid_csuite_gate', True, 'CSUITE_GATE' if step.step_type not in {'cycle','unresolved','limit'} else 'ROUTING_FIX_REQUIRED', [step], None)
        return ApprovalPlan(requester, 'raid_human_hitl', True, 'HUMAN_HITL', self.resolve_chain(requester,'escalationto')+[ApprovalStep('human_operator','critical severity immediate HITL',None,'human')], None)
