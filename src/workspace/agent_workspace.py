from dataclasses import dataclass, field
from pathlib import Path
from .runtime_policy import RuntimePolicy

@dataclass
class AgentWorkspace:
    workspace_id: str
    agent_id: str
    root_dir: Path
    image: str = 'quectosoft/agent-sandbox:latest'
    network_policy: str = 'default-deny'
    env: dict = field(default_factory=dict)
    runtime_policy: RuntimePolicy = field(default_factory=RuntimePolicy)

    def materialize_layout(self):
        for rel in ('work', 'logs', 'artifacts'):
            (self.root_dir / rel).mkdir(parents=True, exist_ok=True)

    def container_spec(self):
        return {
            'image': self.image,
            'command': ['python', '-m', 'src.ui.backend.main'],
            'workdir': str(self.root_dir / 'work'),
            'mounts': [
                {'source': str(self.root_dir / 'work'), 'target': '/workspace'},
                {'source': str(self.root_dir / 'logs'), 'target': '/workspace/logs'},
                {'source': str(self.root_dir / 'artifacts'), 'target': '/workspace/artifacts'},
            ],
            'env': dict(self.env),
            'runtime_policy': self.runtime_policy.as_dict(),
        }

    def provision(self):
        self.materialize_layout()
        return {
            'workspace_id': self.workspace_id,
            'agent_id': self.agent_id,
            'root_dir': str(self.root_dir),
            'network_policy': self.network_policy,
            'runtime_policy': self.runtime_policy.as_dict(),
            'container_spec': self.container_spec(),
            'status': 'ready',
        }
