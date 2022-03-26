-include .env
export

dev.install:
	@flit install --deps develop --symlink

build:
	@flit build --no-setup-py

publish:
	@flit publish

run:
	@python -m aqua data/report.pdf

lint:
	@mypy aqua
	@flake8 aqua
