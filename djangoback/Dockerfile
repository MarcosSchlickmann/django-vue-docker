FROM python:latest

RUN pip install poetry

WORKDIR /back

COPY poetry.lock /back/
COPY pyproject.toml /back/

RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi

WORKDIR /back/djangoback

CMD python manage.py runserver 0.0.0.0:8080
