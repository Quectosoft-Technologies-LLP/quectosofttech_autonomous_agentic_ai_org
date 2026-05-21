"""Browser MCP Server — Quectosoft Technologies LLP — stub"""
from fastapi import FastAPI
app = FastAPI(title="Browser MCP")
@app.get("/health")
async def health(): return {"status": "ok", "server": "browser_mcp"}
