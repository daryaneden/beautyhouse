run:
# 	gunicorn app.main:app --worker-class uvicorn.workers.UvicornWorker -c gunicorn.confic.py
	uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

mig-create: #создание миграции
	alembic revision --autogenerate -m ${MIGRATION}

mig-apply: #применение миграции
	alembic upgrade head