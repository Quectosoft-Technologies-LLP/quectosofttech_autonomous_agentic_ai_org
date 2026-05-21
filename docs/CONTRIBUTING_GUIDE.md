# Contributing Guide — Quectosoft Technologies LLP

See [CONTRIBUTING.md](../CONTRIBUTING.md) for the full guide.

## Quick Reference

```bash
make setup          # install deps + pre-commit hooks
make docker-up      # start all infrastructure
make health-check   # verify all services healthy
make test           # run all tests
make lint           # ruff + mypy --strict
```

## Adding a New Agent

1. Create a YAML card in `config/agents/catalog/tier{N}_{dept}/{agent_id}.yaml`
2. Follow the schema in `config/agents/_schema.yaml` exactly
3. Ensure `raid_config`, `memory`, `workspace`, and `tools` blocks are present
4. Add unit tests in `tests/unit/test_{agent_id}.py`
5. Run `make test` and `make lint` — both must pass
6. Open a PR with title: `feat(agents): add {name} agent card`
