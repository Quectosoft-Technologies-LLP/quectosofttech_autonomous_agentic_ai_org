# Architecture — Quectosoft Technologies LLP Autonomous Agentic AI Org

**Author:** Subrit Dikshit <subrit@quectosofttech.com>

## Overview

The platform is a fully autonomous, multi-tier AI organisation that mirrors a real company structure — from Board to git commit — with every agent operating within strict governance boundaries enforced by the RAID framework, 5-layer memory isolation, and the OpenClaw DAG orchestration engine.

## Tier Structure

| Tier | Role | Model | Count |
|---|---|---|---|
| T1 Board | Ultimate governance authority | Claude Opus 4 | 3 |
| T2 C-Suite | CEO, CTO, COO, CFO, CLO, CHRO, CMO, CSO | Claude Opus 4 / Hermes 70B | 8 |
| T3 VP | 11 VP agents across all functions | Hermes 70B | 11 |
| T4 Dept | SDLC, Corporate, Pre-Sales agents | Hermes 8B / 70B | 40+ |
| T5 Domain | BFSI, Telecom, Healthcare, Retail, GovTech | Hermes 70B / Claude Opus 4 | 20+ |

## Key Subsystems

- **OpenClaw DAG**: Parallel DAG executor with HITL gates and dependency resolution
- **RAID Engine**: Risk/Assumption/Issue/Dependency scoring, auto-mitigation, HITL triggers
- **5-Layer Memory**: L1 private → L2 team → L3 dept → L4 project → L5 org
- **MCP Servers**: 9 typed servers — memory (×5), GitHub, PostgreSQL, Filesystem, Jira
- **Agent Cards**: Every agent defined in YAML — no hardcoded configs in Python
- **Workspace Isolation**: Each agent runs in a dedicated Docker container with NetworkPolicy

## Data Flow

```
Client Request
    → FastAPI /projects
    → OpenClaw DAG (T2 CEO → T3 VP → T4 agents run in parallel)
    → Each agent: policy check → tool calls via MCP → LLM inference → RAID logging
    → RAID score ≥ 20 → HITL pause + Slack/email alert
    → Result aggregated → T2 review → delivery
```
