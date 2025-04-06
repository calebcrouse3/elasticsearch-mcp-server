import logging
import sys

from fastmcp import FastMCP

from src.clients import create_search_client
from src.tools.alias import AliasTools
from src.tools.cluster import ClusterTools
from src.tools.document import DocumentTools
from src.tools.index import IndexTools
from src.tools.register import ToolsRegister

class ElasticsearchMCPServer:
    def __init__(self):
        # Set server name
        self.name = "elasticsearch_mcp_server"
        self.mcp = FastMCP(self.name)
        self.logger = logging.getLogger()
        self.logger.info(f"Initializing {self.name}...")
        
        # Create the Elasticsearch client
        self.search_client = create_search_client()
        
        # Initialize tools
        self._register_tools()

    def _register_tools(self):
        """Register all MCP tools."""
        # Create a tools register
        register = ToolsRegister(self.logger, self.search_client, self.mcp)
        
        # Define all tool classes to register
        tool_classes = [
            IndexTools,
            DocumentTools,
            ClusterTools,
            AliasTools
        ]        
        # Register all tools
        register.register_all_tools(tool_classes)

    def run(self):
        """Run the MCP server."""
        self.mcp.run()

def elasticsearch_mcp_server():
    """Entry point for Elasticsearch MCP server."""
    server = ElasticsearchMCPServer()
    server.run()

if __name__ == "__main__":
    elasticsearch_mcp_server()
