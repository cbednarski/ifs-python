pip=venv/bin/pip
pytest=venv/bin/py.test

init:
	@if [ ! -d venv ]; then virtualenv venv; fi
	$(pip) install -q -r requirements.txt

test: init
	$(pytest) -q tests

freeze:
	$(pip) freeze > requirements.txt