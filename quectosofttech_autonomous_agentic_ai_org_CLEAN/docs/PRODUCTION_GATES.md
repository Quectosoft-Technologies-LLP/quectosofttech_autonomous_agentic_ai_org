# Production Gates

- Source integrity: required orchestration, workspace, UI, deployment, and test assets must exist.
- Quality gates: compile, unit, integration, and e2e tests must pass in CI.
- Runtime gates: health, readiness, memory, RAID, and approval workflows must pass in staging.
- Performance gates: endpoint latency budgets and load-test error budgets must be met.
- Operations gates: logs, metrics, rollback notes, and deployment manifests must be present.
