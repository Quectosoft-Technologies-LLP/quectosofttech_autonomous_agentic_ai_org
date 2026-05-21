from pathlib import Path

def test_release_assets_exist():
    required = [
        'docker/Dockerfile.agent',
        'docker/Dockerfile.memory_mcp',
        'k8s/deployment.yaml',
        'k8s/hpa.yaml',
        '.github/workflows/ci.yml',
        'pytest.ini',
        'src/orchestration/openclaw/dag.py',
        'src/orchestration/openclaw/dag_runner.py',
        'src/workspace/agent_workspace.py',
    ]
    for rel in required:
        assert Path(rel).exists()
