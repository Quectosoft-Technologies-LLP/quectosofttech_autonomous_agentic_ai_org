"""E2E tests — API health check"""
import pytest
from httpx import AsyncClient, ASGITransport
from src.ui.backend.main import app


@pytest.mark.asyncio
async def test_health_endpoint():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        resp = await client.get("/health")
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "ok"
    assert "Quectosoft" in data["platform"]


@pytest.mark.asyncio
async def test_create_project():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        resp = await client.post("/projects", json={
            "client_id": "test_client",
            "objective": "Build a BFSI platform",
            "budget": 100000.0,
            "timeline_days": 90,
            "domain": "BFSI",
        })
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "initiated"
    assert "project_id" in data
