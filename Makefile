t0:
	uvicorn --reload --port 3000 t0__test:app

t1:
	uvicorn --reload --port 3000 t1__upload_file:app