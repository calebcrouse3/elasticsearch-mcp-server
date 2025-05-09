# Elasticsearch MCP Server

## Overview

A Model Context Protocol (MCP) server implementation that provides Elasticsearch interaction. This server enables searching documents and analyzing indices.

## Features

- `list_indices`: List all indices.
- `get_index`: Returns information (mappings, settings, aliases) about one or more indices.
- `search_documents`: Search for documents.
- `get_document`: Get a document by ID.

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


Add the following configuration to Claude Desktop's config file `claude_desktop_config.json`. On macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`.


```json
{
  "mcpServers": {
    "elasticsearch-mcp-server": {
      "command": "uv",
      "args": [
        "--directory",
        "path/to/src/elasticsearch_mcp_server_project",
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

Run the MCP server:

```python
uv run mcp_client/client.py src/server.py
```

Restart Claude Desktop to load the new MCP server.

Now you can interact with your Elasticsearch cluster through Claude using natural language commands like:
