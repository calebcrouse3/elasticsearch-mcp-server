import os

from dotenv import load_dotenv

from src.clients.common.client import SearchClient
from src.clients.exceptions import handle_search_exceptions

def create_search_client() -> SearchClient:
    """
    Create an Elasticsearch client.
    
    Returns:
        An Elasticsearch client instance
    """
    # Load configuration from environment variables
    load_dotenv()
    
    # Get configuration from environment variables
    hosts_str = os.environ.get("ELASTICSEARCH_HOSTS", "https://localhost:9200")
    hosts = [host.strip() for host in hosts_str.split(",")]
    username = os.environ.get("ELASTICSEARCH_USERNAME")
    password = os.environ.get("ELASTICSEARCH_PASSWORD")
    verify_certs = os.environ.get("ELASTICSEARCH_VERIFY_CERTS", "false").lower() == "true"
    
    config = {
        "hosts": hosts,
        "username": username,
        "password": password,
        "verify_certs": verify_certs
    }
    
    return SearchClient(config)

__all__ = [
    'create_search_client',
    'handle_search_exceptions',
    'SearchClient',
]
