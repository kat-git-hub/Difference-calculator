install:
	poetry install
gendiff:
	poetry run python gendiff
lint:
	poetry run flake8 gendiff
build:
	poetry build
publish:
	poetry publish --dry-run
test:
	poetry run pytest -vv
test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml
