tests-unit:
	python -m pytest tests --html=unit-report.html --self-contained-html

tests-e2e: 
	python -m pytest e2e --html=unit-report.html --self-contained-html

tests-e2e-headful: 
	python -m pytest e2e --headful --html=unit-report.html --self-contained-html

pw-dependencies:
	python -m playwright install

run:
	FLASK_APP=flaskr/app.py python -m flask run
