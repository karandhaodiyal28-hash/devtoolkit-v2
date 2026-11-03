.PHONY: help install test lint format build clean publish

PYTHON ?= python

help:
	@echo "install  - install the package and the test dependencies"
	@echo "test     - run the test suite"
	@echo "lint     - run ruff"
	@echo "format   - run ruff format"
	@echo "build    - build the sdist and the wheel"
	@echo "clean    - remove build artefacts"
	@echo "publish  - upload the built distributions to PyPI"

install:
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -e .
	$(PYTHON) -m pip install pytest ruff build

test:
	$(PYTHON) -m pytest tests -q

lint:
	$(PYTHON) -m ruff check src tests

format:
	$(PYTHON) -m ruff format src tests

build: clean
	$(PYTHON) -m build

clean:
	rm -rf build dist .pytest_cache .ruff_cache
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
	find . -type d -name '*.egg-info' -prune -exec rm -rf {} +

publish: build
	$(PYTHON) -m twine upload dist/*
