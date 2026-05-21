"""Confluence MCP Server — Quectosoft Technologies LLP — stub"""
from fastapi import FastAPI
app = FastAPI(title="Confluence MCP")
@app.get("/health")
async def health(): return {"status": "ok", "server": "confluence_mcp"}
