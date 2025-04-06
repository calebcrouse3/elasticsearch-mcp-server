from typing import Dict

from src.clients.base import SearchClientBase

class IndexClient(SearchClientBase):
    def list_indices(self) -> Dict:
        """List all indices."""
        return self.client.cat.indices()
    
    def get_index(self, index: str) -> Dict:
        """Returns information (mappings, settings, aliases) about one or more indices."""
        return self.client.indices.get(index=index)
