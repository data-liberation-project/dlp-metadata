.PHONY: README.md venv data

requirements.txt: requirements.in
	pip-compile requirements.in

venv:
	python -m venv venv
	venv/bin/pip install -r requirements.txt

format:
	black scripts
	isort scripts

lint:
	black --check scripts
	isort --check scripts
	flake8 scripts
	mypy scripts --strict --ignore-missing-imports

data:
	python scripts/extract.py $(DLP_CONTENT_DIR)
