import logging

import typer

from aqua.parsers.parser import TrialParser

logging.basicConfig(level=logging.INFO)

typer_app = typer.Typer(help='Aqua-Parser manager.')


@typer_app.command(help='Start parser.')
def run(filename: str):
    trial = TrialParser()
    trial.parse(filename)


if __name__ == '__main__':
    typer_app()
