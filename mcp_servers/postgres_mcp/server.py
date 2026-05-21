"""PostgreSQL MCP Server — Quectosoft Technologies LLP"""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="PostgreSQL MCP Server", version="0.3.2")

class QueryRequest(BaseModel):
    agent_id: str
    query: str
    params: list = []

@app.get("/health")
async def health():
    return {"status": "ok", "server": "postgres_mcp"}

@app.post("/query")
async def query(req: QueryRequest):
    return {"agent_id": req.agent_id, "rows": [], "status": "stub"}
