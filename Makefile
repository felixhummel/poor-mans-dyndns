MAKEFLAGS += --always-make

default: ruff mypy test

ruff:
	ruff .

mypy:
	mypy .

test:
	pytest --doctest-modules

dev:
	felix-pyenv-virtualenv 3.9
	pip install -U pip
	pip install -e .[dev]
