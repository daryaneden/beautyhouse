run:
	gunicorn app.main:app --worker-class uvicorn.workers.UvicornWorker -c gunicorn.confic.py

mig-create: #создание миграции
	alembic revision --autogenerate -m ${MIGRATION}

mig-apply: #применение миграции
	alembic upgrade head