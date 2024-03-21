test:
	python -m pytest -vv tests . 

lint:
	ruff check src/
	ruff check calculator.py

format:
	ruff format --check src/
	ruff format --check calculator.py

sort:
	ruff check --select I src/
	ruff check --select I calculator.py
