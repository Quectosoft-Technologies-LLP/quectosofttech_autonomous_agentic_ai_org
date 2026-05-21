from dataclasses import dataclass, field
from pathlib import Path
from .runtime_policy import RuntimePolicy

@dataclass
class ProjectWorkspace:
    workspace_id: str
    project_id: str
    root_dir: Path
    members: list[str] = field(default_factory=list)
    runtime_policy: RuntimePolicy = field(default_factory=RuntimePolicy)

    def materialize_layout(self):
        for rel in ('shared', 'logs', 'deliverables'):
            (self.root_dir / rel).mkdir(parents=True, exist_ok=True)

    def container_spec(self):
        return {
            'command': ['python', '-m', 'src.orchestration.openclaw.dag_runner'],
            'workdir': str(self.root_dir / 'shared'),
            'members': list(self.members),
            'runtime_policy': self.runtime_policy.as_dict(),
        }

    def provision(self):
        self.materialize_layout()
        return {
            'workspace_id': self.workspace_id,
            'project_id': self.project_id,
            'root_dir': str(self.root_dir),
            'members': list(self.members),
            'runtime_policy': self.runtime_policy.as_dict(),
            'container_spec': self.container_spec(),
            'status': 'ready',
        }
