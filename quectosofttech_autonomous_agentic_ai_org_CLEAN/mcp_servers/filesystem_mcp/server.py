from pathlib import Path
class MCPServer:
    name='filesystem_mcp'
    def __init__(self, base_dir='.'): self.base_dir=Path(base_dir).resolve()
    def _resolve(self, rel_path):
        target=(self.base_dir/rel_path).resolve()
        if self.base_dir not in [target,*target.parents]: raise ValueError('path escapes base directory')
        return target
    def read_file(self, rel_path): return self._resolve(rel_path).read_text(encoding='utf-8')
    def health(self): return {'server': self.name, 'status': 'ok', 'base_dir': str(self.base_dir)}
