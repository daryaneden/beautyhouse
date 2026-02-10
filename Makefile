run:
	uvicorn main:app --reload --port 8000

mig-create: #создание миграции
	alembic revision --autogenerate -m ${MIGRATION}

mig-apply: #применение миграции
	alembic upgrade head