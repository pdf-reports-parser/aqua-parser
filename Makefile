-include .env
export

dev.install:
	@poetry install

run:
	@python -m aqua

lint:
	@mypy aqua
	@flake8 aqua
