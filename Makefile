unit:
	python -m pytest tests/

e2e:
	python -m pytest e2e/

run:
	FLASK_APP=flaskr/app.py python -m flask run
