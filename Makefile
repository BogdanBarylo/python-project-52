install:
	poetry install

build:
	./build.sh

dev:
	poetry run python3 manage.py runserver

migrations:
	poetry run python3 manage.py makemigrations

migrate:
	poetry run python3 manage.py migrate

lint:
	poetry run flake8 task_manager

test:
	poetry run manage.py test task_manager

test-coverage:
	python3 coverage run --source='.' manage.py test -v 2 && coverage xml