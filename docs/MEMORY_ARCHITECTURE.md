# Memory Architecture — Quectosoft Technologies LLP

**Author:** Subrit Dikshit <subrit@quectosofttech.com>

## 5-Layer Memory Hierarchy

| Layer | Scope | Backend | Access |
|---|---|---|---|
| L1 Agent Private | Single agent | Redis (hot) + ChromaDB (warm) | Self only |
| L2 Team | Team members | ChromaDB | Team members |
| L3 Department | Department | ChromaDB | Dept + VP + C-Suite + Board |
| L4 Project | Project team | ChromaDB | Assigned agents + VP + C-Suite |
| L5 Organisation | Global | ChromaDB + PostgreSQL audit + Neo4j graph | Read: all · Write: C-Suite + Board |

## MCP Servers

Each layer is served by a dedicated MCP server on a fixed port:

| Server | Port | Scope |
|---|---|---|
| agent_memory_mcp | 9001 | L1 |
| team_memory_mcp | 9002 | L2 |
| dept_memory_mcp | 9003 | L3 |
| project_memory_mcp | 9004 | L4 |
| org_memory_mcp | 9005 | L5 |

All cross-scope access is validated by `AccessController` against `config/access_control/memory_rbac_matrix.yaml`.
