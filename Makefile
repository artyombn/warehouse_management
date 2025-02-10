startlinters:
	black . --exclude '\.venv'
	isort . --skip .venv
	pylint . --ignore=.venv
	mypy . --exclude '\.venv'

startpytest:
	pytest -s -v