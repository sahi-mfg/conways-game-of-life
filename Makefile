install:
	python -m pip install --upgrade pip
	python -m pip install -r requirements.txt


test:
	python -m pytest -v

run-cli:
	python main.py

run-flask-dev:
	export FLASK_APP=app.py
	export FLASK_ENV=development
	flask run