install:
	python -m pip install --upgrade pip
	python -m pip install -r requirements.txt


test:
	python -m pytest -v

run:
	python main.py

run_gui:
	python app.py