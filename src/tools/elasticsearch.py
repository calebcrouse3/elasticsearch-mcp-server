from typing import Dict, List

from fastmcp import FastMCP
from src.client import ElasticsearchClient

class ElasticsearchTools:
    def __init__(self, elasticsearch_client: ElasticsearchClient):
        self.elasticsearch_client = elasticsearch_client

    def register_tools(self, mcp: FastMCP):

        @mcp.tool()
        def list_indices() -> List[Dict]:
            """List all indices with document count and store size."""
            return self.elasticsearch_client.list_indices()
        
        @mcp.tool()
        def list_data_streams() -> Dict:
            """Get data stream information."""
            return self.elasticsearch_client.list_data_streams()

        @mcp.tool()
        def search_documents(index: str, query: dict) -> Dict:
            """
            Search for documents.

            Args:
                index: Name of the index or an index pattern
                query: Search query as a python dict. 
            """
            return self.elasticsearch_client.search(index=index, query=query)
