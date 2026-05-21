<div align="center">

<img src="https://img.shields.io/badge/Quectosoft%20Technologies%20LLP-Autonomous%20Agentic%20AI%20Org-01696f?style=for-the-badge&logo=robot&logoColor=white" alt="Quectosoft Technologies LLP"/>

# 🤖 Quectosoft Technologies LLP
## Autonomous Agentic AI Organisation

### *A fully autonomous, multi-tier AI company that builds software, runs itself, and governs every decision — from Board resolution to git commit.*

[![License: QSAL-1.0](https://img.shields.io/badge/License-QSAL--1.0-01696f.svg?style=flat-square)](LICENSE)
[![Python 3.12+](https://img.shields.io/badge/Python-3.12+-3776AB.svg?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![OpenClaw](https://img.shields.io/badge/Orchestration-OpenClaw-ff6b35?style=flat-square)](https://github.com/quectosofttech)
[![Hermes-3](https://img.shields.io/badge/Agents-Hermes--3%20%7C%20Ollama-7c3aed?style=flat-square)](https://ollama.com)
[![ChromaDB](https://img.shields.io/badge/Memory-ChromaDB%20%7C%20Redis%20%7C%20PG-e63946?style=flat-square)](https://www.trychroma.com)
[![Docker](https://img.shields.io/badge/Runtime-Docker%20%7C%20K8s-2496ED?style=flat-square&logo=docker&logoColor=white)](https://docker.com)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen.svg?style=flat-square)](CONTRIBUTING.md)
[![GitHub Sponsors](https://img.shields.io/badge/Sponsor-❤️-ea4aaa?style=flat-square&logo=github-sponsors)](https://github.com/sponsors/quectosofttech)

<br/>

**Author:** [Subrit Dikshit](mailto:subrit@quectosofttech.com)
**Email:** subrit@gmail.com · subrit@quectosofttech.com
**Organisation:** Quectosoft Technologies LLP · Delhi, India

<br/>

> **Submit a natural-language objective. Watch an entire autonomous organisation — Board, C-Suite, HR, Legal, Finance, Engineering, QA, DevOps, BFSI, Telecom — spring to life, collaborate, govern itself with RAID logs, and deliver production-grade software.**

<br/>

[🚀 Quick Start](#-quick-start) · [🏗️ Architecture](#️-architecture) · [📁 Repo Structure](#-repository-structure) · [🤝 Contribute](#-contributing) · [💼 Sponsors](#-sponsors--commercial-use) · [🙏 Acknowledgements](#-acknowledgements--references) · [📄 License](#-license)

</div>

---

## ✨ What Makes This Different

| Feature | Description |
|---|---|
| 🏢 **Full Corporate Hierarchy** | Board → C-Suite → VP → Director → Agent — 8 authority tiers, every decision routed to correct approver |
| 🤖 **80+ Specialised Agents** | SDLC, HR, Legal, Finance, Admin, Security, Pre-Sales, BFSI, Telecom, Healthcare, Retail, GovTech |
| 📋 **RAID-Governed Autonomy** | Every agent maintains live RAID logs. HITL auto-triggers on severity score thresholds |
| 🧠 **5-Layer Memory Hierarchy** | Agent-private → Team → Department → Project → Organisation, RBAC-gated via MCP |
| 🔒 **Isolated Workspaces** | Every agent, team, dept, and project runs in its own Docker container with network policy |
| 🎯 **Per-Agent Model Selection** | Each agent card specifies its own model (hermes3:1b → claude-opus-4) with task-level overrides |
| 📜 **Agent Identity Cards** | Every agent governed by YAML: org_policy, role, responsibilities, access, skills, tools, RAID config |
| 🔑 **OpenClaw Orchestration** | Parallel DAG execution with HITL gates, full audit trail, non-blocking dependency resolution |
| 🌐 **Domain Verticals** | BFSI (RBI/SEBI/GDPR/DPDP), Telecom, Healthcare (HIPAA), Retail, Manufacturing, GovTech |

---

## 🏗️ Architecture

```
┌──────────────────────────────────────────────────────────────────────┐
│                    CLIENT INTERFACE                                  │
│              REST API · WebSocket · Web UI · CLI                     │
└──────────────────────┬───────────────────────────────────────────────┘
                       │
┌──────────────────────▼───────────────────────────────────────────────┐
│           TIER 1 — BOARD OF DIRECTORS                                │
│      Charter · Ethical Oversight · Strategic Governance              │
└──────────────────────┬───────────────────────────────────────────────┘
                       │ Board Resolution
┌──────────────────────▼───────────────────────────────────────────────┐
│           TIER 2 — C-SUITE                                           │
│   CEO · CTO · COO · CFO · CLO · CHRO · CMO · CSO                    │
└──────┬────────────────────────────────────────────────────────────────┘
       │
┌──────▼────────────────────────────────────────────────────────────────┐
│           TIER 3 — VP LAYER                                           │
│  VP Engineering · VP Ops · VP Finance · VP Legal · VP HR             │
│  VP Product · VP Delivery · VP Treasury · VP Security · VP Infra     │
└──────┬────────────────────────────────────────────────────────────────┘
       │
┌──────▼────────────────────────────────────────────────────────────────┐
│           TIER 4 — DEPARTMENT UNITS                                   │
│                                                                       │
│  SDLC DELIVERY          CORPORATE SUPPORT        DOMAIN VERTICALS    │
│  Requirements           HR (7 agents)            BFSI (8 agents)     │
│  Design                 Legal (6 agents)         Telecom (6)          │
│  Engineering            Finance (6 agents)       Healthcare (5)       │
│  QA & Testing           Admin (5 agents)         Retail (4)           │
│  DevOps & SRE           IT Infra (6 agents)      Manufacturing (4)    │
│  Maintenance            Security & Risk (6)      GovTech (4)          │
│                         Pre-Sales/Sales (4)                           │
│                         Marketing (3 agents)                          │
└──────┬────────────────────────────────────────────────────────────────┘
       │  Every phase crosses →
┌──────▼────────────────────────────────────────────────────────────────┐
│           TIER 5 — SAFETY & GOVERNANCE GATE                           │
│   Ethics · Explainability · VulnScan · RAID Engine · Audit            │
└──────┬────────────────────────────────────────────────────────────────┘
       │
┌──────▼────────────────────────────────────────────────────────────────┐
│           TIER 6 — EXECUTION LAYER                                    │
│   OpenClaw DAG · Hermes-3 Agents · MCP Servers · Docker Sandboxes     │
└──────┬────────────────────────────────────────────────────────────────┘
       │
┌──────▼────────────────────────────────────────────────────────────────┐
│           TIER 7 — MEMORY LAYER  (5 scopes, RBAC-gated via MCP)      │
│   L1 Agent-Private · L2 Team · L3 Dept · L4 Project · L5 Org         │
│          ChromaDB · Redis · PostgreSQL 17 (RLS) · Neo4j               │
└───────────────────────────────────────────────────────────────────────┘
```

### 📋 RAID Governance — Every Agent, Every Task

Every agent maintains a live **RAID Log** (Risks · Assumptions · Issues · Dependencies).
Severity = `likelihood (1–5) × impact (1–5)` — maximum 25.

| Score | Zone | Who Acts |
|---|---|---|
| 1–6 | 🟢 Low | Agent acts **fully autonomously**, logs reasoning |
| 7–12 | 🟡 Medium | **VP-level agent** reviews within 2h |
| 13–19 | 🟠 High | **C-Suite gate** — pipeline paused |
| 20–25 | 🔴 Critical | **Immediate human HITL** — Slack + email fired |

### 🧠 5-Layer Memory (RBAC via MCP)

```
L1 Agent Private  →  Self only              (Redis hot + ChromaDB + PostgreSQL audit)
L2 Team           →  Team members           (team_memory_mcp server)
L3 Department     →  Dept + VP + C-Suite    (dept_memory_mcp server)
L4 Project        →  Assigned team          (project_memory_mcp server)
L5 Organisation   →  All read / C-Suite write (org_memory_mcp server)
```

---

## 🚀 Quick Start

### Prerequisites
- Docker 24+ and Docker Compose
- Python 3.12+
- Ollama — `curl -fsSL https://ollama.ai/install.sh | sh`
- 16GB RAM minimum · 32GB recommended for full stack

### 1 — Clone & Setup
```bash
git clone https://github.com/quectosofttech/quectosofttech_autonomous_agentic_ai_org.git
cd quectosofttech_autonomous_agentic_ai_org
make setup
cp .env.example .env          # add your keys — Ollama works fully offline
```

### 2 — Pull Local Models
```bash
make pull-models
# hermes3:1b  (nano agents — HR ops, notifications)
# hermes3:8b  (standard agents — engineering, admin)
# hermes3:70b (advanced — architects, legal, security)
```

### 3 — Start Infrastructure
```bash
make docker-up
# PostgreSQL · Redis · ChromaDB · Neo4j · 5× Memory MCP Servers
make health-check
```

### 4 — Run Platform
```bash
make run
# API  → http://localhost:8000
# Docs → http://localhost:8000/docs
# UI   → http://localhost:3000
# RAID → http://localhost:8000/raid
```

### 5 — Submit Your First Project
```bash
curl -X POST http://localhost:8000/projects \
  -H "Content-Type: application/json" \
  -d '{
    "client_id": "acme_bank",
    "objective": "Build a BFSI KYC onboarding portal with RBI compliance and audit trail",
    "budget": 45000,
    "timeline_days": 30,
    "domain": "BFSI",
    "privacy_level": "strict"
  }'

# Stream live logs
curl -N http://localhost:8000/projects/{id}/stream
```

---

## 📁 Repository Structure

```
quectosofttech_autonomous_agentic_ai_org/
│
├── README.md                          ← You are here
├── LICENSE                            ← QSAL-1.0 (free education / paid commercial)
├── CONTRIBUTING.md
├── SECURITY.md
├── CODE_OF_CONDUCT.md
├── .env.example
├── docker-compose.yml
├── Makefile
├── pyproject.toml
│
├── config/
│   ├── agents/
│   │   ├── _schema.yaml               ← Agent identity card schema
│   │   └── catalog/
│   │       ├── tier1_board/           ← Board Director agent cards
│   │       ├── tier2_csuite/          ← CEO, CTO, COO, CFO, CLO, CHRO, CMO, CSO
│   │       ├── tier3_vp/              ← 11 VP agent cards
│   │       ├── tier4_sdlc/            ← Requirements → Design → Dev → QA → DevOps
│   │       ├── tier4_corporate/       ← HR, Legal, Finance, Admin, IT Infra, Security
│   │       ├── tier4_presales/        ← Pre-Sales, Sales, Proposal agents
│   │       └── tier5_domain/          ← BFSI, Telecom, Healthcare, Retail, GovTech
│   ├── access_control/
│   │   ├── memory_rbac_matrix.yaml    ← 5-layer memory access rules per band
│   │   ├── rbac_matrix.yaml           ← Tool + action RBAC
│   │   └── tool_permissions.yaml
│   ├── org/
│   │   ├── board_charter.yaml
│   │   ├── corporate_policies.yaml
│   │   ├── departments.yaml           ← Autoscaling rules per dept
│   │   └── tech_radar.yaml
│   └── memory_infrastructure.yaml    ← ChromaDB / Redis / PG / Neo4j topology
│
├── src/
│   ├── agents/
│   │   ├── base_agent.py              ← BaseAgent with RAID + 5-layer memory
│   │   ├── tool_calling_agent.py
│   │   └── hermes_agent.py            ← Hermes-3 agent (OpenClaw-native)
│   ├── orchestration/
│   │   └── openclaw/
│   │       ├── dag.py
│   │       ├── dag_runner.py
│   │       ├── hitl_manager.py
│   │       └── approval_engine.py
│   ├── core/
│   │   ├── agent_loader.py
│   │   ├── policy_enforcer.py
│   │   ├── access_controller.py
│   │   └── model_router.py
│   ├── memory/
│   │   ├── layers/                    ← L1–L5 implementations
│   │   ├── access/                    ← RBAC enforcer + access logger
│   │   ├── bridges/                   ← Cross-scope memory bridges
│   │   └── backends/                  ← Redis, ChromaDB, PostgreSQL, Neo4j
│   ├── raid/
│   │   ├── raid_entry.py              ← Pydantic RAID schema
│   │   ├── raid_scorer.py
│   │   ├── threshold_evaluator.py
│   │   ├── mitigation_engine.py
│   │   ├── hitl_trigger.py
│   │   └── raid_store.py
│   ├── workspace/
│   │   ├── agent_workspace.py         ← Per-agent Docker lifecycle
│   │   ├── project_workspace.py
│   │   └── workspace_registry.py
│   ├── units/
│   │   ├── board/
│   │   ├── csuite/
│   │   ├── vps/
│   │   ├── sdlc/
│   │   ├── corporate/
│   │   ├── presales/
│   │   ├── domains/
│   │   └── safety/
│   └── ui/
│       ├── backend/                   ← FastAPI + WebSocket
│       └── frontend/                  ← React + TypeScript
│           └── components/
│               ├── RAIDView.tsx
│               ├── AgentCard.tsx
│               └── PipelineView.tsx
│
├── mcp_servers/
│   ├── memory_mcp/
│   │   ├── agent_memory_mcp/
│   │   ├── team_memory_mcp/
│   │   ├── dept_memory_mcp/
│   │   ├── project_memory_mcp/
│   │   └── org_memory_mcp/
│   ├── github_mcp/
│   ├── postgres_mcp/
│   ├── filesystem_mcp/
│   ├── jira_mcp/
│   ├── confluence_mcp/
│   └── browser_mcp/
│
├── docker/
│   ├── Dockerfile.agent
│   ├── Dockerfile.sandbox
│   └── Dockerfile.memory_mcp
│
├── k8s/
│   ├── deployment.yaml
│   ├── hpa.yaml
│   ├── network_policies/
│   └── rbac/
│
├── docs/
│   ├── ARCHITECTURE.md
│   ├── AGENT_CARDS.md
│   ├── RAID_FRAMEWORK.md
│   ├── MEMORY_ARCHITECTURE.md
│   ├── OPENCLAW.md
│   ├── DOMAIN_VERTICALS.md
│   ├── SDLC.md
│   ├── SAFETY.md
│   └── CONTRIBUTING_GUIDE.md
│
└── tests/
    ├── unit/
    ├── integration/
    └── e2e/
```

---

## 🧩 Technology Stack

| Layer | Primary | Alternatives |
|---|---|---|
| **Orchestration** | OpenClaw DAG | LangGraph, AutoGen, AgentMesh |
| **Agent Framework** | Hermes-3 (NousResearch) | LangChain, PydanticAI, BeeAI |
| **Local Models** | Ollama (hermes3:1b/8b/70b) | llama.cpp, vLLM, Unsloth, TGI |
| **Cloud Models** | Claude Opus 4, GPT-4.1 | Gemini 2.5 Pro, Groq, Together AI |
| **MCP Servers** | Custom Python MCP SDK | Official Anthropic MCP servers |
| **Memory Hot** | Redis Cluster | DragonflyDB, Memcached |
| **Memory Warm** | ChromaDB (multi-tenant) | Qdrant, Weaviate, Pinecone, Milvus |
| **Memory Cold** | PostgreSQL 17 (RLS) | TimescaleDB, CockroachDB |
| **Org Graph** | Neo4j | AWS Neptune, TigerGraph |
| **Code Sandbox** | Docker / Firecracker | E2B, Kata Containers |
| **Web UI** | FastAPI + React + WebSocket | Next.js, Streamlit, Gradio |
| **Observability** | Prometheus + Grafana | LangSmith, Langfuse, SigNoz |
| **Security Scan** | Bandit + Semgrep + Sage | Snyk, TruffleHog, OWASP DC |
| **Task Queue** | Celery + Redis | Temporal.io, RabbitMQ |
| **CI/CD** | GitHub Actions | GitLab CI, Tekton |

---

## 🤝 Contributing

We welcome contributions from researchers, students, developers, and domain experts worldwide.

```bash
git checkout -b feat/your-feature
make lint && make test
git commit -m "feat(scope): description"
# open PR → we review within 48h
```

**Commit types:** `feat` · `fix` · `docs` · `test` · `refactor` · `chore`

See [CONTRIBUTING.md](CONTRIBUTING.md) for full guidelines, agent card YAML spec, and code standards.

### Ways to Contribute

| Type | What We Need |
|---|---|
| 🐛 Bug Fixes | Orchestration, memory, RAID engine, MCP servers |
| 🤖 New Agent Cards | Domain-specific (BFSI sub-roles, HIPAA Healthcare, GovTech) |
| 🧠 Memory Backends | Qdrant, Weaviate, Pinecone, Milvus adapters |
| 🔌 MCP Servers | Jira, Confluence, SAP, Salesforce, ServiceNow |
| 🏢 Domain Verticals | BFSI regulations, HIPAA, Telecom, GovTech policies |
| 📝 Documentation | Architecture guides, tutorials, agent card examples |
| 🧪 Tests | Unit, integration, e2e for any module |
| 🌐 Translations | README in Hindi, Mandarin, Spanish, Arabic, French |

---

## 💼 Sponsors & Commercial Use

**Free forever for:** students · researchers · educators · hobbyists · non-profits
**Paid for:** any for-profit or commercial use — see [LICENSE](LICENSE)

### Sponsor Tiers

| Tier | Monthly | Benefits |
|---|---|---|
| ☕ Coffee | $10 | Name in SPONSORS.md |
| 🥉 Bronze | $100 | + Logo in README |
| 🥈 Silver | $500 | + Priority issues + commercial use (1 product) |
| 🥇 Gold | $1,500 | + Co-development + white-label + dedicated support |
| 💎 Platinum | Custom | Enterprise partnership · joint IP · custom domain vertical |

[**→ Become a Sponsor**](https://github.com/sponsors/quectosofttech)
Commercial licensing: **subrit@quectosofttech.com**

---

## 🛣️ Roadmap

- [x] v0.1 — SDLC Agent Framework (Requirements → Deploy)
- [x] v0.2 — C-Suite + VP Hierarchy + Executive Dispatcher
- [x] v0.3 — Corporate Support Units (HR, Legal, Finance, Admin, IT Infra, Security)
- [x] v0.3.1 — RAID Governance (all agents, all scopes, full HITL engine)
- [x] v0.3.2 — 5-Layer Memory + Isolated Workspaces + Agent Identity Cards (YAML)
- [ ] v0.4 — OpenClaw DAG runner (production) + Hermes-3 full migration
- [ ] v0.5 — Domain Verticals: BFSI full, Healthcare MVP
- [ ] v0.6 — Fine-tuned domain models (BFSI regulatory corpus 2026)
- [ ] v0.7 — Self-healing and self-improving agents
- [ ] v1.0 — Multi-org federation (agent-to-agent across organisations)

---

## 🙏 Acknowledgements & References

This project was architected, designed, and built with the direct assistance and inspiration of an extraordinary ecosystem of AI tools, research, and open-source communities. We are sincerely and deeply grateful to every one of them.

---

### 🤖 AI Research & Design Assistants

| Tool / Platform | Organisation | Role in This Project |
|---|---|---|
| **[Perplexity AI](https://www.perplexity.ai)** | Perplexity AI Inc. | Our **primary design co-pilot** throughout the entire project. Used for architecture research, devil's advocate analysis, RAID framework design, 5-layer memory spec, agent identity card design, domain vertical planning, and all documentation. Powered by Sonnet 4.6 Thinking. |
| **[Claude](https://www.anthropic.com/claude)** | Anthropic | Large-scale code generation, structured multi-agent architecture reasoning, C-Suite agent logic design. Claude Opus 4 powers our critical-tier agents in production. |
| **[ChatGPT / GPT-4.1](https://openai.com/chatgpt)** | OpenAI | Architecture brainstorming, SDLC phase design, API specification drafting, fallback model for standard agents. |
| **[Kimi AI](https://kimi.ai)** | Moonshot AI | Long-context document reasoning — processing 600K+ character design documents and consolidating architecture specs across sessions. |
| **[Gemini](https://deepmind.google/technologies/gemini/)** | Google DeepMind | Multimodal architecture diagrams, research validation, regulatory compliance spec cross-checking (RBI, SEBI, GDPR, DPDP). |
| **[GitHub Copilot](https://github.com/features/copilot)** | GitHub / Microsoft | Inline code completion during implementation sprints, boilerplate generation, test scaffolding. |
| **[Grok](https://x.ai/grok)** | xAI | Technical Q&A, edge case exploration for RAID threshold design, agent governance pattern validation. |
| **[DeepSeek](https://www.deepseek.com)** | DeepSeek AI | Code-specific reasoning, CUDA optimisation guidance, and open-weights model evaluation for local deployment. |

---

### 🧠 Agent & Orchestration Frameworks

| Framework | Organisation | Contribution |
|---|---|---|
| **[Hermes-3](https://nousresearch.com)** | NousResearch | Core agent execution model. hermes3:8b/70b powers all specialist agents. Best-in-class instruction following and tool-use for agentic workflows. |
| **[LangChain](https://langchain.com)** | LangChain Inc. | Agent base class patterns, tool-calling abstractions, prompt template architecture that inspired our BaseAgent design. |
| **[LangGraph](https://langchain-ai.github.io/langgraph/)** | LangChain Inc. | State machine and DAG design patterns that directly informed our OpenClaw orchestrator architecture. |
| **[CrewAI](https://crewai.com)** | CrewAI Inc. | Role-based agent collaboration and department-of-agents concept — which we extended and evolved with OpenClaw + Hermes. |
| **[AutoGen](https://microsoft.github.io/autogen/)** | Microsoft Research | Multi-agent conversation patterns and hierarchical agent design inspiration. |
| **[OpenHands](https://github.com/All-Hands-AI/OpenHands)** | All Hands AI | The leading open-source agentic software engineer — a primary inspiration and production benchmark. |
| **[SWE-agent](https://github.com/SWE-agent/SWE-agent)** | Princeton NLP | Autonomous software engineering architecture that validated SDLC agent chain feasibility. |
| **[PydanticAI](https://ai.pydantic.dev)** | Pydantic | Type-safe agent output validation shaping our Pydantic v2 schema design throughout. |
| **[AgentStack](https://agentstack.sh)** | AgentStack | Agent scaffolding patterns for production deployment. |
| **[BeeAI](https://github.com/i-am-bee/beeai-framework)** | IBM Research | Enterprise-grade agent architecture patterns and BFSI domain considerations. |

---

### 🗄️ Inference & Local Models

| Technology | Organisation | Contribution |
|---|---|---|
| **[Ollama](https://ollama.ai)** | Ollama Inc. | Local model inference engine making the entire platform runnable completely offline. Our default inference layer. |
| **[Unsloth](https://unsloth.ai)** | Unsloth AI | 2× faster fine-tuning for domain-specific model adaptation (BFSI regulatory corpus, SDLC-specific tuning). |
| **[llama.cpp](https://github.com/ggml-org/llama.cpp)** | Georgi Gerganov | GGUF quantisation and CPU-optimised inference underpinning Ollama's runtime engine. |
| **[vLLM](https://vllm.ai)** | UC Berkeley / vLLM | High-throughput PagedAttention inference for production multi-agent GPU deployments. |
| **[Hugging Face](https://huggingface.co)** | Hugging Face Inc. | Model hub, datasets, and the open-weights movement making local inference viable for everyone. |
| **[DeepSeek Coder](https://www.deepseek.com)** | DeepSeek AI | Open-weights coding model used as an alternative local model for engineering agents. |

---

### 🗃️ Memory & Data Infrastructure

| Technology | Organisation | Contribution |
|---|---|---|
| **[ChromaDB](https://www.trychroma.com)** | Chroma | Multi-tenant vector database powering all 5 layers of our episodic memory system. |
| **[Redis](https://redis.io)** | Redis Ltd. | Hot working memory and task queue backbone for agent state and sprint coordination. |
| **[PostgreSQL](https://www.postgresql.org)** | PostgreSQL Global Dev Group | Cold audit memory with Row-Level Security enforcing agent-level memory isolation at the DB layer. |
| **[Neo4j](https://neo4j.com)** | Neo4j Inc. | Org relationship graph tracking agent hierarchy, project assignments, and memory scope access paths. |
| **[Qdrant](https://qdrant.tech)** | Qdrant | Recommended alternative vector DB backend for high-scale deployments. |

---

### 🔌 MCP & API Infrastructure

| Technology | Organisation | Contribution |
|---|---|---|
| **[Model Context Protocol (MCP)](https://modelcontextprotocol.io)** | Anthropic | The foundational standard for all agent-to-tool and agent-to-memory communication. The nervous system of the entire architecture. |
| **[MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)** | Anthropic | Python implementation used to build all 5 memory MCP servers and all external integration servers. |
| **[FastAPI](https://fastapi.tiangolo.com)** | Sebastián Ramírez | High-performance async API layer powering our backend and WebSocket log streaming. |
| **[Pydantic](https://docs.pydantic.dev)** | Pydantic | Data validation and schema enforcement across all agent cards, RAID entries, and memory schemas. |

---

### 🔐 Security & Compliance

| Tool | Organisation | Contribution |
|---|---|---|
| **[Bandit](https://bandit.readthedocs.io)** | PyCQA | Python SAST — embedded in VulnScan agent for every code generation phase. |
| **[Semgrep](https://semgrep.dev)** | Semgrep Inc. | Multi-language static analysis for security patterns, secret detection, and compliance rules. |
| **[Sage](https://www.helpnetsecurity.com/2026/03/09/open-source-tool-sage-security-layer-ai-agents/)** | Gen Digital | Open-source security interception layer for AI agents — blocks malware, phishing, supply-chain attacks at runtime. |
| **[TruffleHog](https://trufflesecurity.com/trufflehog)** | Truffle Security | Secret scanning across agent-generated code and configuration files. |
| **[OWASP Dependency-Check](https://owasp.org/www-project-dependency-check/)** | OWASP Foundation | SCA for CVE detection in generated dependency trees. |
| **[ShieldGemma](https://ai.google.dev/gemma/docs/shieldgemma)** | Google DeepMind | Content safety classification embedded in our Ethics Agent. |

---

### ☁️ Cloud, DevOps & Observability

| Technology | Organisation | Contribution |
|---|---|---|
| **[Docker](https://www.docker.com)** | Docker Inc. | Container runtime for isolated per-agent, per-team, per-project workspace environments. |
| **[Kubernetes](https://kubernetes.io)** | CNCF | K8s NetworkPolicy for workspace isolation, HPA for agent autoscaling at cluster level. |
| **[GitHub Actions](https://github.com/features/actions)** | GitHub / Microsoft | CI/CD pipeline — lint, type-check, and test on every PR to main. |
| **[Prometheus](https://prometheus.io)** | CNCF | Metrics collection for agent performance, RAID dashboard stats, and cost tracking. |
| **[Grafana](https://grafana.com)** | Grafana Labs | Visualisation dashboards for live agent telemetry and RAID heatmaps. |
| **[Celery](https://docs.celeryq.dev)** | Celery Project | Distributed task queue for async agent scheduling and orchestration. |
| **[Terraform](https://www.terraform.io)** | HashiCorp | Infrastructure-as-code for cloud deployment of agent clusters. |

---

### 📚 Research, Papers & Academic References

| Reference | Where Used |
|---|---|
| *Agentic Software Engineering* · [arXiv:2604.26275](https://arxiv.org/pdf/2604.26275.pdf) | Six-layer reference architecture (Foundation, Memory, ACI, Orchestration, Governance, Safety) underpinning our design. |
| *Multi-Agent Framework Survey* · [arXiv:2601.06223](https://arxiv.org/abs/2601.06223) | Framework comparison (CrewAI vs LangGraph vs AutoGen) informing OpenClaw design. |
| *SWE-bench* · Princeton NLP | Benchmark standard for evaluating autonomous software engineering systems. |
| *IBM Research — Hierarchical Multi-Agent Systems* | Hierarchical agent authority design for enterprise environments. |
| *NeurIPS 2025 Poster 116828* — Multi-Agent Coordination | Episodic memory sharing between heterogeneous agents. |
| *Zenodo:19926986* — Agentic SDLC patterns | Agentic SDLC phase and gate design reference. |
| *Anthropic Responsible AI* | Safety, ethics, and explainability layer design principles. |
| *Google AI Responsible Development* · [ai.google.dev/responsible](https://ai.google.dev/responsible) | Ethics agent content safety and fairness design. |
| *An AI-Led SDLC* · [Microsoft Tech Community](https://techcommunity.microsoft.com/blog/appsonazure/an-ai-led-sdlc) | End-to-end agentic SDLC validation and enterprise patterns. |

---

### 🌟 Special Thanks

| Person / Community | Reason |
|---|---|
| **The global open-source AI community** | Every researcher, engineer, and contributor who published papers, code, blog posts, and ideas that made autonomous agentic AI possible. |
| **Hugging Face Community** | Model hosting, datasets, spaces, and the open-weights movement that makes local inference available to everyone. |
| **All Quectosoft Technologies LLP contributors** | Everyone who has opened an issue, submitted a PR, joined a discussion, or shared this project. You are building this with us. |
| **Our early users and testers** | Students, researchers, and builders who tried early versions and gave honest feedback. |

---

## 📄 License

**QSAL-1.0** — Free for students, researchers, educators, hobbyists, and non-profits.
Commercial and for-profit use requires a license or GitHub sponsorship.
See [LICENSE](LICENSE) for full terms.

---

## 📬 Contact

| Channel | Details |
|---|---|
| 📧 Personal | subrit@gmail.com |
| 📧 Professional | subrit@quectosofttech.com |
| 🌐 Organisation | Quectosoft Technologies LLP, Delhi, India |
| 💬 Discussions | [GitHub Discussions](https://github.com/quectosofttech/quectosofttech_autonomous_agentic_ai_org/discussions) |
| 🐛 Bug Reports | [GitHub Issues](https://github.com/quectosofttech/quectosofttech_autonomous_agentic_ai_org/issues) |
| ❤️ Sponsorship | [GitHub Sponsors](https://github.com/sponsors/quectosofttech) |

---

<div align="center">

**Built with ❤️ by [Subrit Dikshit](mailto:subrit@quectosofttech.com) and Quectosoft Technologies LLP Contributors**

*Empowering students, researchers, and builders to explore the frontier of autonomous AI organisations.*

⭐ **Star this repo if it inspires you. Share it with someone who should build with it.** ⭐

</div>
