install:
	poetry install

build:
	./build.sh

dev:
	python3 -m gunicorn hexlet-code.task_manager.asgi:application -k uvicorn.workers.UvicornWorker