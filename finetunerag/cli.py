import click
from finetunerag.server import start_server


@click.group()
def main():
    pass


@main.command()
def start():
    """Start the FineTuneRAG server."""
    click.echo("finetune-rag started on 3003")
    start_server()


if __name__ == '__main__':
    main()
