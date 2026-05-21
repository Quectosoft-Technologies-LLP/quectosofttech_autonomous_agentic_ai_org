"""
Health Check Script — Quectosoft Technologies LLP
Author: Subrit Dikshit <subrit@quectosofttech.com>

Run: python scripts/health_check.py
"""
import asyncio
import httpx
import sys

SERVICES = {
    "Platform API":        "http://localhost:8000/health",
    "Agent Memory MCP":    "http://localhost:9001/health",
    "Team Memory MCP":     "http://localhost:9002/health",
    "Dept Memory MCP":     "http://localhost:9003/health",
    "Project Memory MCP":  "http://localhost:9004/health",
    "Org Memory MCP":      "http://localhost:9005/health",
    "GitHub MCP":          "http://localhost:9010/health",
    "Postgres MCP":        "http://localhost:9011/health",
    "Filesystem MCP":      "http://localhost:9012/health",
}


async def check_service(name: str, url: str, client: httpx.AsyncClient) -> bool:
    try:
        resp = await client.get(url, timeout=3)
        ok = resp.status_code == 200
        status = "✅" if ok else "❌"
        print(f"  {status} {name:30s} {url}")
        return ok
    except Exception as exc:
        print(f"  ❌ {name:30s} UNREACHABLE — {exc}")
        return False


async def main() -> None:
    print("\n🔍 Quectosoft Technologies LLP — Platform Health Check")
    print("=" * 60)
    async with httpx.AsyncClient() as client:
        results = await asyncio.gather(
            *[check_service(name, url, client) for name, url in SERVICES.items()]
        )
    total = len(results)
    passed = sum(results)
    print(f"\n{'=' * 60}")
    print(f"  Result: {passed}/{total} services healthy")
    if passed < total:
        print("  ⚠️  Some services are down. Run: make docker-up")
        sys.exit(1)
    else:
        print("  🎉 All services healthy!")
        sys.exit(0)


if __name__ == "__main__":
    asyncio.run(main())
