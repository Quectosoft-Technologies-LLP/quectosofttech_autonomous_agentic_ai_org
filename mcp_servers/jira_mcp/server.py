class MCPServer:
    name='jira_mcp'
    def health(self): return {'server': self.name, 'status': 'ok', 'configured': False}
