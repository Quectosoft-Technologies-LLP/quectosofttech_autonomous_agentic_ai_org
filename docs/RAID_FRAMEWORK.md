# RAID Framework — Quectosoft Technologies LLP

**Author:** Subrit Dikshit <subrit@quectosofttech.com>

## What is RAID?

RAID = **R**isks · **A**ssumptions · **I**ssues · **D**ependencies

Every agent logs RAID entries during task execution. Each entry is scored and routed to the correct authority tier.

## Severity Score

```
severity = likelihood (1–5) × impact (1–5)  →  range: 1–25
```

## Escalation Matrix

| Score | Zone | Action |
|---|---|---|
| 1–6 | 🟢 LOW | Auto-mitigate |
| 7–12 | 🟡 MEDIUM | VP review required |
| 13–19 | 🟠 HIGH | C-Suite gate required |
| 20–25 | 🔴 CRITICAL | Human HITL — Slack + email alert fired |

## RAID Areas

`SCHEDULE` · `BUDGET` · `TECHNICAL` · `COMPLIANCE` · `SECURITY` · `REPUTATIONAL`

## Per-Agent Overrides

Each agent card can override thresholds in its `raid_config` block.
Domain agents (BFSI, Healthcare) use tighter thresholds (HITL from 15, not 20).
