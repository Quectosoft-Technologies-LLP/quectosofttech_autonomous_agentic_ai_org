from pathlib import Path
from src.core.access_controller import AccessController
from src.core.agent_loader import AgentLoader
from src.core.mcp_registry import MCPRegistry
from src.core.model_router import ModelRouter
from src.core.policy_enforcer import PolicyEnforcer
from src.core.settings import AppSettings
from src.memory.service import MemoryService
from src.observability.service import ObservabilityService
from src.orchestration.openclaw.approval_engine import ApprovalEngine
from src.orchestration.openclaw.hitl_manager import HITLManager
from src.raid.hitl_trigger import HITLTrigger
from src.raid.mitigation_engine import MitigationEngine
from src.raid.raid_store import RAIDStore
from src.raid.threshold_evaluator import ThresholdEvaluator

class RuntimeServices:
    def __init__(self, repo_root: str | Path):
        self.settings = AppSettings.from_repo_root(repo_root)
        schema_path = self.settings.repo_root / 'config/agents/_schema.yaml'
        catalog_root = self.settings.repo_root / 'config/agents/catalog'
        self.loader = AgentLoader(schema_path, catalog_root)
        self.cards = self.loader.load_all(strict=True)
        self.policy = PolicyEnforcer(self.cards)
        self.access = AccessController(self.policy)
        self.models = ModelRouter()
        self.approvals = ApprovalEngine(self.cards, self.policy)
        self.raid_store = RAIDStore(self.settings.db_path)
        self.raid_thresholds = ThresholdEvaluator(self.approvals)
        self.raid_mitigation = MitigationEngine()
        self.hitl_trigger = HITLTrigger()
        self.hitl_manager = HITLManager()
        self.memory = MemoryService(self.policy, self.settings.db_path)
        self.mcps = MCPRegistry(self.settings.repo_root, self.settings.db_path)
        self.observability = ObservabilityService(self.settings.log_dir)
        self._summary_cache = {
            'agent_count': len(self.cards),
            'schema_issues': len(self.loader.validate_all()),
            'relationship_issues': len(self.loader.validate_relationships(self.cards)),
            'db_path': str(self.settings.db_path),
            'log_dir': str(self.settings.log_dir),
        }
        self._mcp_health_cache = self.mcps.health()
        self.observability.metrics.set_value('agents_loaded_total', len(self.cards))
    def summary(self):
        return dict(self._summary_cache)
    def mcp_health(self):
        return dict(self._mcp_health_cache)
