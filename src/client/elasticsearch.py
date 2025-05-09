import logging
import warnings
from typing import Dict

class ElasticsearchClient():
    def __init__(self, config: Dict):
        """
        Initialize the Elasticsearch client.
        
        Args:
            config: Configuration dictionary with connection parameters
        """
        self.logger = logging.getLogger()
        self.config = config
        
        # Extract common configuration
        host = config.get("host")
        username = config.get("username")
        password = config.get("password")
        api_key = config.get("api_key")
        verify_certs = config.get("verify_certs", False)
        
        # Disable insecure request warnings if verify_certs is False
        if not verify_certs:
            warnings.filterwarnings("ignore", message=".*verify_certs=False is insecure.*")
            warnings.filterwarnings("ignore", message=".*Unverified HTTPS request is being made to host.*")
            
            try:
                import urllib3
                urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            except ImportError:
                pass
        
        # Initialize Elasticsearch client
        from elasticsearch import Elasticsearch
        self.client = Elasticsearch(
            hosts=host,
            basic_auth=(username, password) if username and password else None,
            verify_certs=verify_certs,
            api_key=api_key,
            retry_on_timeout=True,
            request_timeout=30
        )
        self.logger.info(f"Elasticsearch client initialized with host: {host}")

    def list_indices(self) -> list[dict]:
        """List all indices."""
        resp = self.client.cat.indices(format="json")
        index_names = [{"index": index['index'], "docs.count": index['docs.count'], "store.size": index['store.size']} for index in resp.body]
        return index_names

    def list_data_streams(self) -> Dict:
        """Returns the data stream for an index."""
        resp = self.client.indices.data_streams_stats()
        return resp.body

    def search(self, index: str, query: dict) -> Dict:
        """Execute a search query."""
        size = query.get("size", None)
        if not size or size > 20:
            return {"error": "Query size must be less than or equal to 20"}

        resp = self.client.search(index=index, body=query)
        return resp.body
