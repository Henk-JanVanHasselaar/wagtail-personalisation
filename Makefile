.PHONY: all clean requirements develop test lint flake8 isort dist sandbox docs

all: clean requirements dist

default: develop

clean:
	find src -name '*.pyc' -delete
	find tests -name '*.pyc' -delete
	find . -name '*.egg-info' -delete

requirements:
	pip install --upgrade -e .[docs,test]

install: develop

develop: clean requirements

test:
	py.test --nomigrations --reuse-db tests/

retest:
	py.test --nomigrations --reuse-db tests/ -vvv

coverage:
	py.test --nomigrations --reuse-db tests/ --cov=wagtail_personalisation --cov-report=term-missing --cov-report=html

docs:
	$(MAKE) -C docs html

lint: flake8 isort

flake8:
	flake8 src/ tests/

isort:
	pip install isort
	isort --recursive src tests

dist:
	./setup.py sdist bdist_wheel

sandbox:
	pip install -r sandbox/requirements.txt
	sandbox/manage.py migrate
	sandbox/manage.py loaddata sandbox/exampledata/users.json
	sandbox/manage.py loaddata sandbox/exampledata/personalisation.json
	sandbox/manage.py runserver

release:
	pip install twine wheel
	rm -rf dist/*
	python setup.py sdist bdist_wheel
	twine upload -s dist/*
