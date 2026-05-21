# Agent Cards — Quectosoft Technologies LLP

**Author:** Subrit Dikshit <subrit@quectosofttech.com>

## What is an Agent Card?

An Agent Card is a YAML file in `config/agents/catalog/` that fully defines an agent's:
- Identity (id, name, tier, department, role)
- Model assignment (default + per-task overrides)
- Memory scope access (L1–L5)
- Workspace isolation settings
- RAID thresholds (per-agent overrides)
- Allowed tools
- Skills
- Applicable org policies

**No agent configuration lives in Python code.** All agent identity is in YAML cards.

## Schema

See `config/agents/_schema.yaml` for the full schema with field descriptions.

## Catalog Structure

```
config/agents/catalog/
├── tier1_board/      3 cards
├── tier2_csuite/     8 cards (CEO, CTO, COO, CFO, CLO, CHRO, CMO, CSO)
├── tier3_vp/        11 cards
├── tier4_sdlc/       7 cards (Requirements → Design → Dev → QA → DevOps → Security → Docs)
├── tier4_corporate/  8 cards (HR, Legal, Finance, IT, Security, Admin)
├── tier4_presales/   3 cards
└── tier5_domain/     9 cards (BFSI×3, Telecom×2, Healthcare×2, Retail, GovTech)
```
