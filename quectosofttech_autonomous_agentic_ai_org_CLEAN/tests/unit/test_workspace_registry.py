from src.workspace.workspace_registry import WorkspaceRegistry

def test_workspace_registry_creates_agent_workspace(tmp_path):
    registry = WorkspaceRegistry(tmp_path)
    ws = registry.create_agent_workspace('backend_engineer')
    assert ws['status'] == 'ready'
    assert ws['runtime_policy']['network_policy'] == 'default-deny'
    assert ws['container_spec']['workdir'].endswith('/work')
