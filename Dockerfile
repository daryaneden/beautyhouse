FROM python:3.12-slim

WORKDIR /app

# Отключаем создание виртуальных окружений Poetry и задаем PYTHONPATH
ENV POETRY_VIRTUALENVS_CREATE=false \
    PYTHONPATH=/app

COPY pyproject.toml poetry.lock* /app/

RUN pip install --no-cache-dir poetry \
    && poetry install --no-root --no-interaction --no-ansi

COPY . /app

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
