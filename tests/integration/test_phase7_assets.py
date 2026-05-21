from pathlib import Path

def test_phase7_assets_exist():
    required = [
        'src/observability/exporters.py',
        'src/workspace/runtime_policy.py',
        'k8s/canary.yaml',
        'k8s/pdb.yaml',
        '.env.example',
        'docs/GO_NO_GO.md',
        'docs/LOAD_TESTING.md',
    ]
    for rel in required:
        assert Path(rel).exists()
