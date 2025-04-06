from typing import Dict

from src.clients.base import SearchClientBase

class DocumentClient(SearchClientBase):
    def search_documents(self, index: str, body: Dict) -> Dict:
        """Search for documents in the index."""
        return self.client.search(index=index, body=body)
  
    def get_document(self, index: str, id: str) -> Dict:
        """Get a document by ID."""
        return self.client.get(index=index, id=id)
