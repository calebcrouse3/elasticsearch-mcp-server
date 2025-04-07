import logging
import sys

from fastmcp import FastMCP

from src.client import create_elasticsearch_client
from src.tools.elasticsearch import ElasticsearchTools
from src.tools.register import ToolsRegister

class ElasticsearchMCPServer:
    def __init__(self):
        # Set server name
        self.name = "elasticsearch_mcp_server"
        self.mcp = FastMCP(self.name)
        self.logger = logging.getLogger()
        self.logger.info(f"Initializing {self.name}...")
        
        # Create the Elasticsearch client
        self.elasticsearch_client = create_elasticsearch_client()
        
        # Initialize tools
        self._register_tools()

    def _register_tools(self):
        """Register all MCP tools."""
        # Create a tools register
        register = ToolsRegister(self.logger, self.elasticsearch_client, self.mcp)

        # Register all tools
        register.register_tools(ElasticsearchTools)

    def run(self):
        """Run the MCP server."""
        self.mcp.run()

def elasticsearch_mcp_server():
    """Entry point for Elasticsearch MCP server."""
    server = ElasticsearchMCPServer()
    server.run()

if __name__ == "__main__":
    elasticsearch_mcp_server()
