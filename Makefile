tests-unit:
	python -m pytest tests

tests-e2e: 
	python -m pytest e2e/ --headful

run:
	FLASK_APP=flaskr/app.py python -m flask run
