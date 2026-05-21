import json, sqlite3
from dataclasses import dataclass
from pathlib import Path
from src.memory.access.access_logger import AccessLogger

@dataclass
class MemoryWriteResult:
    layer: str
    key: str
    written: bool

class MemoryService:
    def __init__(self, policy_enforcer, db_path: str | Path):
        self.policy_enforcer = policy_enforcer; self.db_path = Path(db_path); self.db_path.parent.mkdir(parents=True, exist_ok=True); self.logger = AccessLogger(); self._init_db()
    def _conn(self): return sqlite3.connect(self.db_path)
    def _init_db(self):
        with self._conn() as conn:
            conn.execute('CREATE TABLE IF NOT EXISTS memory_items (layer TEXT, memory_key TEXT, payload TEXT NOT NULL, PRIMARY KEY(layer,memory_key))'); conn.commit()
    def read(self, agent_id: str, layer: str, key: str):
        d = self.policy_enforcer.can_use_memory_layer(agent_id, layer, 'read'); self.logger.log(agent_id=agent_id, layer=layer, mode='read', allowed=d.allowed)
        if not d.allowed: raise PermissionError(d.reason)
        with self._conn() as conn: row = conn.execute('SELECT payload FROM memory_items WHERE layer = ? AND memory_key = ?', (layer,key)).fetchone()
        return None if row is None else json.loads(row[0])
    def write(self, agent_id: str, layer: str, key: str, value):
        d = self.policy_enforcer.can_use_memory_layer(agent_id, layer, 'write'); self.logger.log(agent_id=agent_id, layer=layer, mode='write', allowed=d.allowed)
        if not d.allowed: raise PermissionError(d.reason)
        with self._conn() as conn: conn.execute('INSERT OR REPLACE INTO memory_items (layer, memory_key, payload) VALUES (?, ?, ?)', (layer,key,json.dumps(value))); conn.commit()
        return MemoryWriteResult(layer, key, True)
