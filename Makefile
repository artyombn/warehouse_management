startlinters:
	black . --exclude '\.venv'
	isort . --skip .venv
	pylint . --ignore=.venv

startpytest:
	pytest -s -v