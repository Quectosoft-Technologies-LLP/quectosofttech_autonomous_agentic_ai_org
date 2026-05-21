"""Filesystem MCP Server — Quectosoft Technologies LLP"""
import os
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Filesystem MCP Server", version="0.3.2")
WORKSPACE_ROOT = os.getenv("WORKSPACE_ROOT", "/tmp/quecto_workspaces")

class FileRequest(BaseModel):
    agent_id: str
    path: str
    content: str = ""

@app.get("/health")
async def health():
    return {"status": "ok", "server": "filesystem_mcp"}

@app.post("/write")
async def write_file(req: FileRequest):
    safe = os.path.join(WORKSPACE_ROOT, req.agent_id, req.path.lstrip("/"))
    os.makedirs(os.path.dirname(safe), exist_ok=True)
    with open(safe, "w") as f:
        f.write(req.content)
    return {"status": "written", "path": safe}

@app.get("/read/{agent_id}/{path:path}")
async def read_file(agent_id: str, path: str):
    safe = os.path.join(WORKSPACE_ROOT, agent_id, path)
    if not os.path.exists(safe):
        return {"content": None, "error": "not_found"}
    return {"content": open(safe).read()}
