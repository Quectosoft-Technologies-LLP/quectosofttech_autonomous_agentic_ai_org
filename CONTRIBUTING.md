# Contributing to Quectosoft Technologies LLP — Autonomous Agentic AI Org

**Author & Maintainer:** Subrit Dikshit
**Email:** subrit@gmail.com · subrit@quectosofttech.com
**Organisation:** Quectosoft Technologies LLP · Delhi, India

Thank you for your interest in contributing! Every PR, issue, discussion, and idea makes this platform better for the entire community.

---

## Before You Start

- Read the [README](README.md) to understand the full architecture.
- Check [open issues](https://github.com/quectosofttech/quectosofttech_autonomous_agentic_ai_org/issues) — your idea may already be tracked.
- For large features or new domain verticals, open a **Discussion** first to align before coding.

---

## Setup

```bash
git clone https://github.com/YOUR_USERNAME/quectosofttech_autonomous_agentic_ai_org.git
cd quectosofttech_autonomous_agentic_ai_org
make setup          # installs deps + pre-commit hooks
cp .env.example .env
make docker-up      # start PostgreSQL, Redis, ChromaDB, Neo4j, MCP servers
make health-check   # verify everything is running
make test           # all tests must pass before your PR
```

---

## Ways to Contribute

| Type | What We Need |
|---|---|
| 🐛 Bug Fixes | Orchestration, RAID engine, memory layers, MCP servers |
| 🤖 New Agent Cards | Domain agents (BFSI sub-roles, HIPAA Healthcare, GovTech) |
| 🧠 Memory Backends | Qdrant, Weaviate, Pinecone, Milvus adapters |
| 🔌 MCP Servers | Jira, Confluence, SAP, Salesforce, ServiceNow integrations |
| 🏢 Domain Verticals | BFSI regulatory rules, HIPAA, Telecom specs, GovTech policies |
| 📝 Documentation | Architecture guides, tutorials, agent card examples |
| 🧪 Tests | Unit, integration, e2e for any module |
| 🌐 Translations | README in Hindi, Mandarin, Spanish, Arabic, French |

---

## Commit Convention

```
feat(scope): short description of what was added
fix(scope):  what was broken and how it is now fixed
docs(scope): what documentation changed
test(scope): what tests were added or updated
refactor(scope): what changed without behaviour modification
chore(scope): build, dependency, or tooling change

Examples:
  feat(agents/bfsi): add CKYC verification agent with RBI tokenisation
  fix(raid): threshold evaluator not applying COMPLIANCE area override
  docs(memory): update 5-layer memory hierarchy guide with Neo4j section
  test(openclaw): add parallel DAG branch integration tests
```

---

## Pull Request Checklist

- [ ] `make lint` passes (ruff + mypy --strict)
- [ ] `make test` passes — all existing and new tests green
- [ ] New agent cards follow `config/agents/_schema.yaml` exactly
- [ ] RAID `raid_config` block present in every new agent card
- [ ] Memory `memory` block present in every new agent card
- [ ] Workspace `workspace` block present in every new agent card
- [ ] Docstrings on all public methods and classes
- [ ] `docs/` updated if you changed any architecture or design
- [ ] No hardcoded secrets — all config via `.env`
- [ ] No hardcoded agent configurations in Python — YAML cards only

---

## Code Standards

- Python 3.12+, fully typed everywhere (`mypy --strict`)
- Pydantic v2 for all data models — no raw dicts for structured data
- All agent identity defined in YAML cards — no hardcoded agent configs in Python
- Tests: unit + integration for every new agent, tool, and MCP server
- One test file per source file, mirroring the `src/` directory structure

---

## Questions?

Open a [GitHub Discussion](https://github.com/quectosofttech/quectosofttech_autonomous_agentic_ai_org/discussions)
or email: **subrit@quectosofttech.com**
