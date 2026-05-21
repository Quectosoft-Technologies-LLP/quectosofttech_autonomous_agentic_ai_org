class MCPServer:
    name='confluence_mcp'
    def health(self): return {'server': self.name, 'status': 'ok', 'configured': False}
