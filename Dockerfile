FROM python:3.11-slim-buster

WORKDIR /app

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN pip install pipenv
RUN pipenv install --system

# CMD ["python3", "manage.py", "runserver", "0.0.0.0:3000"]