"""
Seed Org Memory — Quectosoft Technologies LLP
Author: Subrit Dikshit <subrit@quectosofttech.com>

Seeds L5 organisation memory with policies, tech radar, and org chart.
Run: python scripts/seed_org_memory.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.memory.layers.l5_org_memory import L5OrgMemory

SEED_DOCS = [
    ("org:mission",     "Quectosoft Technologies LLP builds fully autonomous AI organisations."),
    ("org:values",      "Transparency, Safety, Innovation, Compliance, Privacy-first."),
    ("org:tech_stack",  "Hermes-3, Ollama, OpenClaw DAG, FastAPI, ChromaDB, Redis, PostgreSQL, Neo4j, MCP."),
    ("org:raid_policy", "RAID severity >= 20 triggers HITL. 13-19 requires C-Suite gate. 7-12 VP review."),
    ("org:memory",      "5-layer memory: L1 agent-private, L2 team, L3 department, L4 project, L5 org."),
]


def main() -> None:
    print("🌱 Seeding L5 Organisation Memory...")
    mem = L5OrgMemory()
    for doc_id, text in SEED_DOCS:
        mem.store(doc_id, text, metadata={"source": "seed_script", "version": "0.3.2"})
        print(f"  ✅ {doc_id}")
    print(f"\n✅ Seeded {len(SEED_DOCS)} documents into L5 org memory.")


if __name__ == "__main__":
    main()
