# Safety Architecture — Quectosoft Technologies LLP

**Author:** Subrit Dikshit <subrit@quectosofttech.com>

## Defence-in-Depth Layers

1. **Agent isolation**: Every agent runs in a Docker container with read-only FS,
   no privilege escalation, and dropped Linux capabilities.
2. **Network isolation**: K8s NetworkPolicy — agents can only reach their assigned
   MCP servers. No direct agent-to-agent TCP.
3. **Memory RBAC**: PostgreSQL Row-Level Security ensures no agent can read
   another agent's private memory at the database layer.
4. **RAID governance**: Automatic escalation prevents autonomous agents from
   taking high-impact actions without human or C-Suite approval.
5. **Code sandbox**: All agent-generated code executes in Dockerfile.sandbox —
   no network, no apt, no pip, no host mounts.
6. **Static analysis**: Bandit, Semgrep, and Sage scan every code artifact before
   it enters the repository.
7. **Audit trail**: All memory reads/writes and RAID entries are persisted to
   PostgreSQL with timestamps and agent identity for full audit replay.
8. **HITL**: Any RAID score ≥ 20 pauses the DAG and fires Slack + email alerts
   to human operators before execution continues.
