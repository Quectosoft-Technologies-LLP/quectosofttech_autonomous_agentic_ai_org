# OpenClaw DAG Orchestration — Quectosoft Technologies LLP

**Author:** Subrit Dikshit <subrit@quectosofttech.com>

## What is OpenClaw?

OpenClaw is Quectosoft's proprietary DAG-based orchestration engine.
It replaces LangChain/CrewAI with a typed, policy-enforced, HITL-aware parallel executor.

## Core Concepts

- **DAGNode**: A single agent task with declared dependencies
- **DAGRunner**: Resolves ready nodes, runs them in parallel via `asyncio.gather`
- **HITL Gate**: A node blocks when its RAID score hits threshold — human must approve to resume
- **ApprovalEngine**: Routes each RAID score to the correct approver tier

## Example DAG: SDLC Pipeline

```
requirements_agent
    └── architect_agent
            ├── developer_agent (×N parallel)
            │       └── qa_engineer_agent (×N parallel)
            │               └── devops_agent
            └── security_eng_agent  ← parallel with developer
```

Each edge represents a dependency. OpenClaw runs all nodes with no unresolved
dependencies simultaneously, collapsing multi-day human pipelines into minutes.
