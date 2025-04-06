from typing import Dict

from src.clients.common.alias import AliasClient
from src.clients.common.cluster import ClusterClient
from src.clients.common.document import DocumentClient
from src.clients.common.index import IndexClient

class SearchClient(IndexClient, DocumentClient, ClusterClient, AliasClient):
    """
    Unified Elasticsearch client that combines all search functionality.
    
    This class uses multiple inheritance to combine all specialized client implementations
    (index, document, cluster, alias) into a single unified client.
    """
    
    def __init__(self, config: Dict):
        """
        Initialize the Elasticsearch client.
        
        Args:
            config: Configuration dictionary with connection parameters
        """
        super().__init__(config)
        self.logger.info("Initialized the Elasticsearch client")
