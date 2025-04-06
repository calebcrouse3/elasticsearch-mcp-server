from typing import Dict

from src.clients.base import SearchClientBase

class AliasClient(SearchClientBase):
    def list_aliases(self) -> Dict:
        """Get all aliases."""
        return self.client.cat.aliases()
    
    def get_alias(self, index: str) -> Dict:
        """Get aliases for the specified index."""
        return self.client.indices.get_alias(index=index)
