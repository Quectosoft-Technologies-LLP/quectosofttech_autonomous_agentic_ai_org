from dataclasses import dataclass, asdict
from .policy_enforcer import PolicyEnforcer

@dataclass
class AccessRequest:
    agent_id: str
    action_type: str
    resource: str

class AccessController:
    def __init__(self, policy_enforcer: PolicyEnforcer):
        self.policy_enforcer = policy_enforcer
        self.audit_log = []
    def authorize(self, request: AccessRequest):
        decision = self.policy_enforcer.can_access(request.agent_id, request.action_type, request.resource)
        self.audit_log.append({'request': asdict(request), 'decision': asdict(decision)})
        return decision
