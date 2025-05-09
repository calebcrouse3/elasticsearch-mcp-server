import logging

from fastmcp import FastMCP

from src.client import ElasticsearchClient
from src.client.exceptions import with_exception_handling
from src.tools.elasticsearch import ElasticsearchTools

class ToolsRegister:
    """Class to handle registration of MCP tools."""
    
    def __init__(self, logger: logging.Logger, elasticsearch_client: ElasticsearchClient, mcp: FastMCP):
        """
        Initialize the tools register.
        
        Args:
            logger: Logger instance
            search_client: Search client instance
            mcp: FastMCP instance
        """
        self.logger = logger
        self.elasticsearch_client = elasticsearch_client
        self.mcp = mcp
    
    def register_tools(self, tool_class: ElasticsearchTools):
        """
        Register all tools with the MCP server.
        
        Args:
            tool_classes: List of tool classes to register
        """

        self.logger.info(f"Registering tools from {tool_class.__name__}")
        tool_instance = tool_class(self.elasticsearch_client)
        
        # Register tools with automatic exception handling
        with_exception_handling(tool_instance, self.mcp)
