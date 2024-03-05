install:
	poetry install

build:
	./build.sh

dev:
	python3 -m gunicorn task_manager.asgi:application -k uvicorn.workers.UvicornWorker