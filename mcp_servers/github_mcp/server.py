class MCPServer:
    name='github_mcp'
    def health(self): return {'server': self.name, 'status': 'ok', 'token_configured': False}
