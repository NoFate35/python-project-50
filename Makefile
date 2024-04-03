install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=python-project-50 --cov-report xml

lint:
	poetry run flake8

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

.PHONY: install test lint selfcheck check build
