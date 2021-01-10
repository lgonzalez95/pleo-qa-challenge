unit:
	python -m pytest src/test

e2e:
	pytest tests/e2e

run:
	FLASK_APP=src/app.py flask run
