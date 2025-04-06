from typing import Dict

from fastmcp import FastMCP

class DocumentTools:
    def __init__(self, search_client):
        self.search_client = search_client
    
    def register_tools(self, mcp: FastMCP):
        @mcp.tool()
        def search_documents(index: str, body: Dict) -> Dict:
            """
            Search for documents.
            
            Args:
                index: Name of the index
                body: Search query
            """
            return self.search_client.search_documents(index=index, body=body)

        @mcp.tool()
        def get_document(index: str, id: str) -> Dict:
            """
            Get a document by ID.
            
            Args:
                index: Name of the index
                id: Document ID
            """
            return self.search_client.get_document(index=index, id=id)
