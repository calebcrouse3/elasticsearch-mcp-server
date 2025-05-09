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


@cli.command(name="get-index-mappings")
@click.option(
    '--index', '-i',
    type=str,
    help='Index name'
)
def get_index_mappings(index: str):
    """Get index information."""
    es_client = create_elasticsearch_client()
    result = es_client.get_index_mappings(index)
    click.echo(type(result))
    click.echo(result)


@cli.command(name="get-index-settings")
@click.option(
    '--index', '-i',
    type=str,
    help='Index name'
)
def get_index_settings(index: str):
    """Get index information."""
    es_client = create_elasticsearch_client()
    result = es_client.get_index_settings(index)
    click.echo(type(result))
    click.echo(result)


@cli.command(name="list-data-stream")
@click.option(
    '--index', '-i',
    type=str,
    help='Index name'
)
def list_data_streams():
    """Get index information."""
    es_client = create_elasticsearch_client()
    result = es_client.list_data_streams()
    click.echo(type(result))
    click.echo(result)


@cli.command(name="search")
@click.option(
    '--index', '-i',
    type=str,
    help='Index name'
)
@click.option(
    '--query', '-q',
    type=str,
    help='Query'
)
def search(index: str, query: str):
    """Get index information."""
    es_client = create_elasticsearch_client()
    result = es_client.search(index, query)
    click.echo(type(result))
    click.echo(result)


if __name__ == '__main__':
    cli() 