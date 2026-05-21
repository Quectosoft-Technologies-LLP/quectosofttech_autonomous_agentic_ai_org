from pathlib import Path
class MCPServer:
    name='postgres_mcp'
    def __init__(self, db_path='data/runtime.db'): self.db_path=str(Path(db_path))
    def health(self): return {'server': self.name, 'status': 'ok', 'db_path': self.db_path}
