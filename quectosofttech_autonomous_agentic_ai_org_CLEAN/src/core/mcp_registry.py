from mcp_servers.browser_mcp.server import MCPServer as BrowserMCP
from mcp_servers.confluence_mcp.server import MCPServer as ConfluenceMCP
from mcp_servers.filesystem_mcp.server import MCPServer as FilesystemMCP
from mcp_servers.github_mcp.server import MCPServer as GitHubMCP
from mcp_servers.jira_mcp.server import MCPServer as JiraMCP
from mcp_servers.postgres_mcp.server import MCPServer as PostgresMCP

class MCPRegistry:
    def __init__(self, repo_root, db_path):
        self.github = GitHubMCP(); self.postgres = PostgresMCP(db_path=db_path); self.filesystem = FilesystemMCP(base_dir=repo_root); self.jira = JiraMCP(); self.confluence = ConfluenceMCP(); self.browser = BrowserMCP()
    def health(self):
        return {'github': self.github.health(),'postgres': self.postgres.health(),'filesystem': self.filesystem.health(),'jira': self.jira.health(),'confluence': self.confluence.health(),'browser': self.browser.health()}
