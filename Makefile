install:
	poetry install

build:
	./build.sh

dev:
	cd hexlet-code && python3 -m gunicorn task_manager.asgi:application -k uvicorn.workers.UvicornWorker