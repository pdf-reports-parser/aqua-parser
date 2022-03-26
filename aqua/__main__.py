import logging

import typer

from aqua.parser import TocParser

logging.basicConfig(level=logging.INFO)

typer_app = typer.Typer(help='Aqua-Parser manager.')


@typer_app.command(help='Start parser.')
def run(filename: str):
    parser = TocParser()
    parser.parse(filename=filename)


if __name__ == '__main__':
    typer_app()
