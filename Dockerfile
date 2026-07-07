FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml /app/

RUN pip3 install poetry

RUN poetry install

COPY . /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
