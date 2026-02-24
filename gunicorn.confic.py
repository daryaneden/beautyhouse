from uvicorn.workers import UvicornWorker

bind = 'localhost:8080'
workers = 4
default_worker_class = UvicornWorker
