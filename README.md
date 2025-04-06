# Elasticsearch MCP Server

## Overview

A Model Context Protocol (MCP) server implementation that provides Elasticsearch interaction. This server enables searching documents, analyzing indices, and managing cluster through a set of tools.

## Features

### Index Operations

- `list_indices`: List all indices.
- `get_index`: Returns information (mappings, settings, aliases) about one or more indices.
- `create_index`: Create a new index.
- `delete_index`: Delete an index.

### Document Operations

- `search_documents`: Search for documents.
- `index_document`: Creates or updates a document in the index.
- `get_document`: Get a document by ID.
- `delete_document`: Delete a document by ID.
- `delete_by_query`: Deletes documents matching the provided query.

### Cluster Operations

- `get_cluster_health`: Returns basic information about the health of the cluster.
- `get_cluster_stats`: Returns high-level overview of cluster statistics.

### Alias Operations

- `list_aliases`: List all aliases.
- `get_alias`: Get alias information for a specific index.
- `put_alias`: Create or update an alias for a specific index.
- `delete_alias`: Delete an alias for a specific index.

## Configure Environment Variables

Copy the `.env.example` file to `.env` and update the values accordingly.

## Start Elasticsearch Cluster

Start the Elasticsearch cluster using Docker Compose:

```bash
docker-compose -f docker-compose-elasticsearch.yml up -d
```

The default Elasticsearch username is `elastic` and password is `test123`.

You can access Kibana from http://localhost:5601.

## Usage with Claude Desktop

### Using uv with local development

Using `uv` requires cloning the repository locally and specifying the path to the source code. Add the following configuration to Claude Desktop's config file `claude_desktop_config.json`.

```json
{
  "mcpServers": {
    "elasticsearch-mcp-server": {
      "command": "uv",
      "args": [
        "--directory",
        "path/to/src/elasticsearch_mcp_server",
        "run",
        "elasticsearch-mcp-server"
      ],
      "env": {
        "ELASTICSEARCH_HOST": "https://localhost:9200",
        "ELASTICSEARCH_USERNAME": "elastic",
        "ELASTICSEARCH_PASSWORD": "test123"
      }
    }
  }
}
```

- On macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- On Windows: `%APPDATA%/Claude/claude_desktop_config.json`

Restart Claude Desktop to load the new MCP server.

Now you can interact with your Elasticsearch cluster through Claude using natural language commands like:
- "List all indices in the cluster"
- "How old is the student Bob?"
- "Show me the cluster health status"

## Usage with Anthropic MCP Client

```python
uv run mcp_client/client.py src/server.py
```

## License

This project is licensed under the Apache License Version 2.0 - see the [LICENSE](LICENSE) file for details.
