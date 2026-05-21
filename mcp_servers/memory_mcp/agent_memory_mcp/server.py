class MCPServer:
    name = 'l1_memory_mcp'
    layer = 'l1'
    def __init__(self, memory_service=None): self.memory_service = memory_service
    def read(self, agent_id: str, key: str):
        if self.memory_service is None: raise RuntimeError('memory service not attached')
        return self.memory_service.read(agent_id, self.layer, key)
    def write(self, agent_id: str, key: str, value):
        if self.memory_service is None: raise RuntimeError('memory service not attached')
        return self.memory_service.write(agent_id, self.layer, key, value)
    def health(self): return {'server': self.name, 'status': 'ok', 'attached': self.memory_service is not None, 'layer': self.layer}
