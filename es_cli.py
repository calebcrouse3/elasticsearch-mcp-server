#!/usr/bin/env python3

import json
import os
import sys
import click
from src.client import create_elasticsearch_client

@click.group()
@click.version_option(version="0.1.0")
def cli():
    """Command-line interface for Elasticsearch client operations."""
    pass


@cli.command(name="list-indices")
def list_indices():
    """List all indices."""
    es_client = create_elasticsearch_client()
    result = es_client.list_indices()
    click.echo(type(result))
    click.echo(result)

    
@cli.command(name="get-index")
@click.option(
    '--index', '-i',
    type=str,
    help='Index name'
)
def get_index(index: str):
    """Get index information."""
    es_client = create_elasticsearch_client()
    result = es_client.get_index(index)
    click.echo(type(result))
    click.echo(result)


if __name__ == '__main__':
    cli() 