test:
	python -m pytest -vv tests . 

lint:
	ruff check src/
	ruff check calculator.py

format:
	ruff format --check src/
	ruff format --check calculator.py

sort:
	ruff sort --check src/
	ruff sort --check calculator.py
