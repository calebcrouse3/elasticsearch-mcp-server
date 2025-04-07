from typing import Dict, Optional, List

from fastmcp import FastMCP
import logging
from src.client import ElasticsearchClient

class ElasticsearchTools:
    def __init__(self, elasticsearch_client: ElasticsearchClient):
        self.elasticsearch_client = elasticsearch_client

    def register_tools(self, mcp: FastMCP):

        @mcp.tool()
        def list_indices() -> List[Dict]:
            """List all indices."""
            return self.elasticsearch_client.list_indices()

        @mcp.tool()
        def get_index(index: str) -> Dict:
            """
            Returns information (mappings, settings, aliases) about one or more indices.
            
            Args:
                index: Name of the index
            """
            return self.elasticsearch_client.get_index(index=index)

        # @mcp.tool()
        # def search_documents(index: str, body: Dict) -> Dict:
        #     """
        #     Search for documents.
            
        #     Args:
        #         index: Name of the index
        #         body: Search query
        #     """
        #     return self.elasticsearch_client.search_documents(index=index, body=body)

        # @mcp.tool()
        # def get_document(index: str, id: str) -> Dict:
        #     """
        #     Get a document by ID.
            
        #     Args:
        #         index: Name of the index
        #         id: Document ID
        #     """
        #     return self.elasticsearch_client.get_document(index=index, id=id)
        
        # @mcp.tool()
        # def get_cluster_health() -> Dict:
        #     """Returns basic information about the health of the cluster."""
        #     return self.elasticsearch_client.get_cluster_health()

        # @mcp.tool()
        # def get_cluster_stats() -> Dict:
        #     """Returns high-level overview of cluster statistics."""
        #     return self.elasticsearch_client.get_cluster_stats()
        
        # @mcp.tool()
        # def list_aliases() -> List[Dict]:
        #     """List all aliases."""
        #     return self.elasticsearch_client.list_aliases()

        # @mcp.tool()
        # def get_alias(index: str) -> Dict:
        #     """
        #     Get alias information for a specific index.

        #     Args:
        #         index: Name of the index
        #     """
        #     return self.elasticsearch_client.get_alias(index=index)
