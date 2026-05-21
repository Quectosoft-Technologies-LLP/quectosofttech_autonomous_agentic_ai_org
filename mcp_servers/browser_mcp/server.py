class MCPServer:
    name='browser_mcp'
    def health(self): return {'server': self.name, 'status': 'ok'}
