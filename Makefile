t0:
	uvicorn --reload --port 3000 t0__test:app

t1:
	uvicorn --reload --port 3000 t1__upload_file:app

t2:
	uvicorn --reload --port 3000 t2__async_sync:app

t3:
	uvicorn --reload --port 3000 t3__jinja:app