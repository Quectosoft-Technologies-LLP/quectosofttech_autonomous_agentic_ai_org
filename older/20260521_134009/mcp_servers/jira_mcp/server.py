"""Jira MCP Server — Quectosoft Technologies LLP — stub"""
from fastapi import FastAPI
app = FastAPI(title="Jira MCP")
@app.get("/health")
async def health(): return {"status": "ok", "server": "jira_mcp"}
