from dataclasses import asdict, is_dataclass
from pathlib import Path
from typing import Any
import asyncio

try:
    from fastapi import FastAPI, HTTPException, WebSocket
    from fastapi.responses import PlainTextResponse
except Exception:
    class HTTPException(Exception):
        def __init__(self, status_code: int, detail: str):
            super().__init__(detail)
            self.status_code = status_code
            self.detail = detail
    class WebSocket:
        async def accept(self):
            return None
        async def send_json(self, _payload):
            return None
        async def close(self):
            return None
    class FastAPI:
        def __init__(self, title: str = ''):
            self.title = title
        def get(self, _path: str, **_kwargs):
            return lambda fn: fn
        def post(self, _path: str, **_kwargs):
            return lambda fn: fn
        def websocket(self, _path: str, **_kwargs):
            return lambda fn: fn
    class PlainTextResponse(str):
        def __new__(cls, value: str = ''):
            return str.__new__(cls, value)

from pydantic import BaseModel
from src.core.access_controller import AccessRequest
from src.core.runtime import RuntimeServices
from src.observability.tracing import new_trace_id
from src.raid.raid_entry import RAIDEntry

BASE_DIR = Path(__file__).resolve().parents[3]
services = RuntimeServices(BASE_DIR)
app = FastAPI(title='Quectosoft Autonomous Agentic AI Org')

class EventStream:
    def __init__(self):
        self.events: list[dict[str, Any]] = []
    def publish(self, event: dict[str, Any]):
        self.events.append(event)
        if len(self.events) > 500:
            self.events = self.events[-500:]
    def snapshot(self):
        return list(self.events)

event_stream = EventStream()

def _normalize(v):
    if is_dataclass(v):
        return asdict(v)
    if isinstance(v, dict):
        return {k: _normalize(x) for k, x in v.items()}
    if isinstance(v, list):
        return [_normalize(x) for x in v]
    return v

def _record(event_type, metric_name, **payload):
    trace_id = new_trace_id()
    event = {'name': event_type, 'trace_id': trace_id, **payload}
    services.observability.record(event_type, metric_name, **event)
    event_stream.publish({'event_type': event_type, **event})
    return trace_id

class WorkflowPayload(BaseModel):
    agent_id: str
    action_type: str
    resource: str
    operation: str

class MemoryWritePayload(BaseModel):
    agent_id: str
    layer: str
    key: str
    value: dict

class RAIDPayload(BaseModel):
    entry_id: str
    agent_id: str
    task_id: str
    raid_type: str
    title: str
    description: str
    likelihood: int
    impact: int
    category: str = 'GENERAL'

@app.get('/health')
def health():
    trace_id = _record('health_check', 'api_health_requests_total')
    return {'status': 'ok', 'trace_id': trace_id, 'summary': services.summary(), 'mcp_health': services.mcp_health()}

@app.get('/ready')
def ready():
    trace_id = _record('readiness_check', 'api_readiness_requests_total')
    return {'status': 'ready', 'trace_id': trace_id, 'db_path': services.summary()['db_path']}

@app.get('/metrics', response_class=PlainTextResponse)
def metrics():
    services.observability.metrics.set_value('raid_entries_total', len(services.raid_store.list()))
    return services.observability.metrics.prometheus_text()

@app.get('/events')
def events():
    trace_id = _record('events_snapshot', 'api_events_snapshot_total')
    snapshot = event_stream.snapshot()
    return {'trace_id': trace_id, 'count': len(snapshot), 'events': snapshot[-50:]}

@app.websocket('/ws/events')
async def ws_events(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_json({
        'type': 'hello',
        'status': 'connected',
        'agents': services.summary()['agent_count'],
        'trace_id': new_trace_id(),
        'recent_events': event_stream.snapshot()[-10:],
    })
    for _ in range(3):
        await asyncio.sleep(0.05)
        snapshot = event_stream.snapshot()
        await websocket.send_json({
            'type': 'heartbeat',
            'trace_id': new_trace_id(),
            'event_count': len(snapshot),
            'recent_events': snapshot[-5:],
        })
    await websocket.send_json({'type': 'complete', 'trace_id': new_trace_id()})
    await websocket.close()

@app.post('/workflows/access-approval')
def access_approval_workflow(payload: WorkflowPayload):
    trace_id = _record('access_approval_workflow', 'api_workflow_access_approval_total', agent_id=payload.agent_id)
    access = services.access.authorize(AccessRequest(payload.agent_id, payload.action_type, payload.resource))
    approval = services.approvals.get_operation_plan(payload.agent_id, payload.operation)
    return {'trace_id': trace_id, 'access': _normalize(access), 'approval': _normalize(approval)}

@app.post('/memory/write')
def memory_write(payload: MemoryWritePayload):
    trace_id = _record('memory_write', 'api_memory_write_total', agent_id=payload.agent_id, layer=payload.layer)
    return {'trace_id': trace_id, 'result': _normalize(services.memory.write(payload.agent_id, payload.layer, payload.key, payload.value))}

@app.get('/memory/read/{agent_id}/{layer}/{key}')
def memory_read(agent_id: str, layer: str, key: str):
    trace_id = _record('memory_read', 'api_memory_read_total', agent_id=agent_id, layer=layer)
    return {'trace_id': trace_id, 'value': services.memory.read(agent_id, layer, key)}

@app.post('/raid/evaluate')
def raid_evaluate(payload: RAIDPayload):
    trace_id = _record('raid_evaluate', 'api_raid_evaluate_total', agent_id=payload.agent_id)
    entry = RAIDEntry(**payload.model_dump())
    services.raid_store.add(entry)
    decision = services.raid_thresholds.evaluate(entry)
    mitigation = services.raid_mitigation.suggest(entry, services.cards[payload.agent_id].data.get('raidconfig', {}))
    channels = services.hitl_trigger.channels_for(decision.action)
    services.observability.metrics.set_value('raid_entries_total', len(services.raid_store.list()))
    return {'trace_id': trace_id, 'entry': entry.model_dump(mode='json'), 'decision': _normalize(decision), 'mitigation': _normalize(mitigation), 'channels': channels}
