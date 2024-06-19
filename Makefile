MAKEFLAGS += --always-make

default: ruff mypy test

ruff:
	ruff .

mypy:
	mypy .

test:
	pytest --doctest-modules

dev:
	felix-pyenv-virtualenv 3.12
	pip install -U pip
	pip install -e .[dev]

requirements.txt:
	uv pip compile pyproject.toml -o requirements.txt
