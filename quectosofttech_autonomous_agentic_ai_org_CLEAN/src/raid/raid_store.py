import json, sqlite3
from pathlib import Path

class RAIDStore:
    def __init__(self, db_path: str | Path):
        self.db_path = Path(db_path); self.db_path.parent.mkdir(parents=True, exist_ok=True); self._init_db()
    def _conn(self): return sqlite3.connect(self.db_path)
    def _init_db(self):
        with self._conn() as conn:
            conn.execute('CREATE TABLE IF NOT EXISTS raid_entries (entry_id TEXT PRIMARY KEY, agent_id TEXT, payload TEXT NOT NULL, created_at TEXT)'); conn.commit()
    def add(self, entry):
        payload = entry.model_dump(mode='json') if hasattr(entry, 'model_dump') else dict(entry)
        with self._conn() as conn:
            conn.execute('INSERT OR REPLACE INTO raid_entries (entry_id, agent_id, payload, created_at) VALUES (?, ?, ?, ?)', (payload['entry_id'], payload['agent_id'], json.dumps(payload), str(payload.get('created_at','')))); conn.commit()
    def list(self, agent_id=None):
        with self._conn() as conn:
            rows = conn.execute('SELECT payload FROM raid_entries' + (' WHERE agent_id = ?' if agent_id else ''), (agent_id,) if agent_id else ()).fetchall()
        return [json.loads(r[0]) for r in rows]
