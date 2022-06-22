setup:
	python -m venv environments/venv
	. environments/venv/bin/activate
	pip install --upgrade pip
	pip install -r requirements.dev
	

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -f .coverage
	rm -f .coverage.*

clean: clean-pyc clean-test

test: clean
	. environments/venv/bin/activate
	python -m pytest -v --cov=ariaria --cov-report=term-missing --cov-fail-under 10

mypy:
	. environments/venv/bin/activate
	python -m mypy ariaria

lint:
	. environments/venv/bin/activate 
	python -m pylint ariaria -j 4 --reports=y

docs: FORCE
	cd docs; . environments/venv/bin/activate && sphinx-apidoc -o ./source ./ariaria
	cd docs; . environments/venv/bin/activate && sphinx-build -b html ./source ./build
FORCE:

check: test mypy lint



