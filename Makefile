install:
	poetry install

build:
	./build.sh

dev:
	python3 manage.py runserver