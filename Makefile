pip=venv/bin/pip
pytest=venv/bin/py.test

init:
	virtualenv venv
	$(pip) install -r requirements.txt

test:
	$(pytest) tests

freeze:
	$(pip) freeze > requirements.txt