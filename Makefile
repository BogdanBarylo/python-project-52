install:
	poetry install

build:
	./build.sh

dev:
	python3 manage.py runserver

migrations:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate

lint:
	poetry run flake8 task_manager

test:
	python3 manage.py test task_manager

test-coverage:
	coverage run --source='.' manage.py test -v 2 && coverage xml
