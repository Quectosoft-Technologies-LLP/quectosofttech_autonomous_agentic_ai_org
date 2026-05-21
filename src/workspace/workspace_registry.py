from pathlib import Path
from .agent_workspace import AgentWorkspace
from .project_workspace import ProjectWorkspace

class WorkspaceRegistry:
    def __init__(self, base_dir: str | Path):
        self.base_dir = Path(base_dir)
        self.base_dir.mkdir(parents=True, exist_ok=True)
        self.workspaces = {}

    def create_agent_workspace(self, agent_id: str):
        ws = AgentWorkspace(workspace_id=f'agent-{agent_id}', agent_id=agent_id, root_dir=self.base_dir / 'agents' / agent_id)
        self.workspaces[ws.workspace_id] = ws.provision()
        return self.workspaces[ws.workspace_id]

    def create_project_workspace(self, project_id: str, members: list[str]):
        ws = ProjectWorkspace(workspace_id=f'project-{project_id}', project_id=project_id, root_dir=self.base_dir / 'projects' / project_id, members=members)
        self.workspaces[ws.workspace_id] = ws.provision()
        return self.workspaces[ws.workspace_id]

    def list_workspaces(self):
        return dict(self.workspaces)
