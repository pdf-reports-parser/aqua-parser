-include .env
export

dev.install:
	@flit install --deps develop --symlink

build:
	@flit build --no-setup-py

publish:
	@flit publish

run:
	@python -m aqua

lint:
	@mypy aqua
	@flake8 aqua
