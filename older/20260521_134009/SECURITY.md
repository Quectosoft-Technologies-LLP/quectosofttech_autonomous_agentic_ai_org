# Security Policy

**Author & Maintainer:** Subrit Dikshit
**Email:** subrit@quectosofttech.com
**Organisation:** Quectosoft Technologies LLP · Delhi, India

---

## Supported Versions

| Version | Supported |
|---|---|
| main (latest) | ✅ Active support |
| Latest tagged release | ✅ Active support |
| Older branches | ❌ Not supported |

---

## Reporting a Vulnerability

**Do NOT open a public GitHub issue for security vulnerabilities.**

Email: **subrit@quectosofttech.com**
Subject line: `[SECURITY] <brief one-line description>`

Please include:
- Clear description of the vulnerability
- Step-by-step reproduction instructions
- Impact assessment (what can an attacker do?)
- Suggested fix or mitigation (if known)

We will acknowledge within **48 hours** and aim to deliver a patch within **14 days**.

---

## Security Architecture

- Every agent container runs in a fully isolated Docker network — no direct inter-agent TCP
- All cross-agent and cross-scope communication happens exclusively via typed MCP tool calls
- MCP servers validate access policy on every single call — no blind passthrough
- PostgreSQL Row-Level Security enforces agent-level memory isolation at the database layer
- All secrets loaded from environment variables — never hardcoded, never logged
- Bandit + Semgrep + Sage scan all agent-generated code before execution in sandbox
- K8s NetworkPolicy objects enforce workspace isolation at cluster level in production
- Agent containers run with read-only root filesystem and no privilege escalation
