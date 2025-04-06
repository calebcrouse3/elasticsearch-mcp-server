from typing import Dict, Optional, List

from fastmcp import FastMCP

class IndexTools:
    def __init__(self, search_client):
        self.search_client = search_client
        
    def register_tools(self, mcp: FastMCP):
        @mcp.tool()
        def list_indices() -> List[Dict]:
            """List all indices."""
            return self.search_client.list_indices()

        @mcp.tool()
        def get_index(index: str) -> Dict:
            """
            Returns information (mappings, settings, aliases) about one or more indices.
            
            Args:
                index: Name of the index
            """
            return self.search_client.get_index(index=index)
