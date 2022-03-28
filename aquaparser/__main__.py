import logging

import typer

from aquaparser import parser

logging.basicConfig(level=logging.INFO)

typer_app = typer.Typer(help='Aqua-Parser manager.')


@typer_app.command(help='Start parser.')
def run(filename: str):
    measurement = parser(filename)


if __name__ == '__main__':
    typer_app()
