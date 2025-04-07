import os
from pathlib import Path

from dotenv import load_dotenv

from src.client.elasticsearch import ElasticsearchClient
from src.client.exceptions import handle_search_exceptions

def create_elasticsearch_client() -> ElasticsearchClient:
    """
    Create an Elasticsearch client.
    
    Returns:
        An Elasticsearch client instance
    """
    # Load configuration from environment variables
    root_dir = Path(__file__).resolve().parents[2]
    env_path = os.path.join(root_dir, ".env")
    if os.path.exists(env_path):
        load_dotenv(dotenv_path=env_path)
    else:
        raise FileNotFoundError(f"No .env file found at {env_path}")

    # This might need to be here to make the env in the server definition work.  
    # load_dotenv()

    # Get configuration from environment variables
    host = os.environ.get("ELASTICSEARCH_HOST")
    username = os.environ.get("ELASTICSEARCH_USERNAME")
    password = os.environ.get("ELASTICSEARCH_PASSWORD")
    api_key = os.environ.get("ELASTICSEARCH_API_KEY")
    verify_certs = os.environ.get("ELASTICSEARCH_VERIFY_CERTS", "false").lower() == "true"
    
    if not host:
        raise ValueError("ELASTICSEARCH_HOST is not set")
    if not api_key:
        raise ValueError("ELASTICSEARCH_API_KEY is not set")

    config = {
        "host": host,
        "username": username,
        "password": password,
        "api_key": api_key,
        "verify_certs": verify_certs
    }
    
    return ElasticsearchClient(config)

__all__ = [
    'create_elasticsearch_client',
    'handle_search_exceptions'
]

