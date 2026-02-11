FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 PIP_NO_CACHE_DIR=1

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY . /app

RUN mkdir -p /artifacts

CMD ["pytest", "-q", "tests/framework_frontend/test", "-m", "not gui", "--disable-warnings", "--junitxml=/artifacts/junit.xml"]
