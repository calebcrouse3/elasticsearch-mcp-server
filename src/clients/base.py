from abc import ABC
import logging
import warnings
from typing import Dict

class SearchClientBase(ABC):
    def __init__(self, config: Dict):
        """
        Initialize the Elasticsearch client.
        
        Args:
            config: Configuration dictionary with connection parameters
        """
        self.logger = logging.getLogger()
        self.config = config
        
        # Extract common configuration
        hosts = config.get("hosts")
        username = config.get("username")
        password = config.get("password")
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
            hosts=hosts,
            basic_auth=(username, password) if username and password else None,
            verify_certs=verify_certs
        )
        self.logger.info(f"Elasticsearch client initialized with hosts: {hosts}")
