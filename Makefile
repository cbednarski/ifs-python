pip=venv/bin/pip
pytest=venv/bin/py.test

init:
	@if [ ! -d venv ]; then virtualenv venv; fi
	$(pip) install -q -r requirements.txt
	$(pip) install .

test: init
	$(pytest) -q tests

freeze:
	$(pip) freeze > requirements.txt

publish:
	python setup.py register
	python setup.py sdist upload
